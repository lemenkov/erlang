#!/bin/bash
# Usage:
#    ./otp-get-patches.sh /path/to/otp OTP_R14B01 fedora-R14B01
#
# otp-get-patches.sh - update erlang.spec and otp-00*.patch files
#
# otp-get-patches.sh updates the erlang.spec and otp-00*.patch
# files in the git index. After an otp-get-patches.sh run, you
# will need to review the stage git changes, possibly adapt the
# Release: and %changelog parts of erlang spec, and can then
# "git commit" everything.
#
# Caution: Leave the four special comment lines untouched in the
# spec file, as otp-get-patches.sh requires them and will only
# touch erlang.spec between the respective start/end pair:
#
# # start of autogenerated patch tag list
# # end of autogenerated patch tag list
# # start of autogenerated prep patch list
# # end of autogenerated prep patch list
#
# The following special comment lines in the git commit messages
# will be interpreted:
#
#    Fedora-Spec-Comment: This patch only applies to EL6 builds
#    Fedora-Spec-Before: %if 0%?el6}
#    Fedora-Spec-After: %endif
#
# If there is no "Fedora-Spec-Comment:" line, we will use
# "Fedora specific patch".

# Command line parsing
otp_dir="${1:?'Fatal: otp git repo dir required'}"
otp_upstream="${2:?'Fatal: git ref to upstream release required'}"
otp_fedora="${3:?'Fatal: git ref to branch with fedora patches required'}"

# Setup
set -e
# set -x
tmpdir="$(mktemp -d --tmpdir="$PWD")"

# Generate patch files
pushd "$otp_dir"
git format-patch -o "$tmpdir" "${otp_upstream}..${otp_fedora}" > "$tmpdir/patch-list.txt"
popd

test -s "$tmpdir/patch-list.txt"

# Process patch files
echo "# start of autogenerated patch tag list" > "$tmpdir/patch-list-tags.txt"
echo "# start of autogenerated prep patch list" > "$tmpdir/patch-list-prep.txt"
n=1
while read patch
do
	otppatch="$(dirname "$patch")/otp-$(basename "$patch")"
	mv -f "$patch" "$otppatch"
	comment="$(sed -n 's/^Fedora-Spec-Comment:\s*//p' "$otppatch")"
	if test "x$comment" = "x"; then comment="Fedora specific patch"; fi
	echo "# ${comment}" >> "$tmpdir/patch-list-tags.txt"
	echo "#   $(sed -n 's/^Subject: \[PATCH /\[/p' "$otppatch")" >> "$tmpdir/patch-list-tags.txt"
	echo "Patch$n: $(basename "$otppatch")" >> "$tmpdir/patch-list-tags.txt"
	base="$(basename "$patch" ".patch" | sed 's/^00[0-9][0-9]-//')"
	backupext=".$(echo -n "$base" | tr -c -s '[:alnum:]' '_')"
	sed -n 's/^Fedora-Spec-Before:\s*//p' "$otppatch" >> "$tmpdir/patch-list-prep.txt"
	echo "%patch$n -p1 -b ${backupext}" >> "$tmpdir/patch-list-prep.txt"
	sed -n 's/^Fedora-Spec-After:\s*//p' "$otppatch" >> "$tmpdir/patch-list-prep.txt"
	n=$(($n + 1))
done < "$tmpdir/patch-list.txt"
echo "# end of autogenerated patch tag list" >> "$tmpdir/patch-list-tags.txt"
echo "# end of autogenerated prep patch list" >> "$tmpdir/patch-list-prep.txt"

# Create updated spec file
specfile="erlang.spec"
newspec1="${tmpdir}/${specfile}.new1"
newspec2="${tmpdir}/${specfile}.new2"
sed '/^# start of autogenerated patch tag list$/,$d' "$specfile" > "$newspec1"
cat "$tmpdir/patch-list-tags.txt" >> "$newspec1"
sed '1,/^# end of autogenerated patch tag list/d' "$specfile" >> "$newspec1"
sed '/^# start of autogenerated prep patch list$/,$d' "$newspec1" > "$newspec2"
cat "$tmpdir/patch-list-prep.txt" >> "$newspec2"
sed '1,/^# end of autogenerated prep patch list/d' "$newspec1" >> "$newspec2"

# Actually put all changes into git index
git rm -f otp-00*.patch
mv "$tmpdir/otp-00"*.patch .
git add otp-00*.patch
mv -f "$newspec2" "$specfile"
git add "$specfile"

rm -rf "$tmpdir"
# End of file.
