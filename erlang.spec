%define ver R13B
%define rel 04

Name:           erlang
Version:        %{ver}
Release:        %{rel}.3%{?dist}
Summary:        General-purpose programming language and runtime environment

Group:          Development/Languages
License:        ERPL
URL:            http://www.erlang.org
Source:         http://www.erlang.org/download/otp_src_%{ver}%{rel}.tar.gz
Source1:        http://www.erlang.org/download/otp_doc_html_%{ver}%{rel}.tar.gz
Source2:        http://www.erlang.org/download/otp_doc_man_%{ver}%{rel}.tar.gz
Source3:	erlang-find-provides.escript
Source4:	erlang-find-provides.sh
Source5:	erlang-find-requires.escript
Source6:	erlang-find-requires.sh
Source7:	macros.erlang
# TODO this patch needs rebase against current tree
Patch0:         otp-links.patch
Patch1:		otp-0001-Do-not-format-man-pages.patch
Patch2:		otp-0002-Remove-rpath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:	zlib-devel
BuildRequires:  unixODBC-devel
BuildRequires:  wxGTK-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	java-1.6.0-openjdk-devel
BuildRequires:  flex
BuildRequires:	m4
BuildRequires:	fop

Requires:       tk

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.


%package doc
Summary:	Erlang documentation
Group:		Development/Languages

%description doc
Documentation for Erlang.


%prep
%setup -q -n otp_src_%{ver}%{rel}
%patch1 -p1 -b .do_not_format_manpages
%patch2 -p1 -b .rpath
# remove shipped zlib sources
rm -f erts/emulator/zlib/*.[ch]


%build
%ifarch sparcv9 sparc64
CFLAGS="$RPM_OPT_FLAGS -mcpu=ultrasparc -fno-strict-aliasing" %configure --enable-shared-zlib
%else
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %configure --enable-shared-zlib
%endif
make


%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_PREFIX=$RPM_BUILD_ROOT install

# clean up
find $RPM_BUILD_ROOT%{_libdir}/erlang -perm 0775 | xargs chmod 755
find $RPM_BUILD_ROOT%{_libdir}/erlang -name Makefile | xargs chmod 644
find $RPM_BUILD_ROOT%{_libdir}/erlang -name \*.o | xargs chmod 644
find $RPM_BUILD_ROOT%{_libdir}/erlang -name \*.bat | xargs rm -f
find $RPM_BUILD_ROOT%{_libdir}/erlang -name index.txt.old | xargs rm -f

# install additional doc files
mkdir -p erlang_doc
tar -C erlang_doc -zxf %{SOURCE1}

# install man-pages
tar -C $RPM_BUILD_ROOT%{_libdir}/erlang -zxf %{SOURCE2}
gzip $RPM_BUILD_ROOT%{_libdir}/erlang/man/man*/*

# make links to binaries
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cd $RPM_BUILD_ROOT%{_bindir}
for file in erl erlc escript dialyzer
do
  ln -sf ../%{_lib}/erlang/bin/$file .
done

# remove buildroot from installed files
cd $RPM_BUILD_ROOT%{_libdir}/erlang
sed -i "s|$RPM_BUILD_ROOT||" erts*/bin/{erl,start} releases/RELEASES bin/{erl,start}

# remove unneeded sources, but keep *.hrl and *.yrl
for d in $RPM_BUILD_ROOT%{_libdir}/erlang/lib/* ; do find $d/src -maxdepth 1 -type f ! -name "*.hrl" -print -delete || true ; done
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/hipe-*/{cerl,flow,icode,main,misc,util}/*.erl
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/orber-*/COSS/CosNaming/*.erl
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/snmp-*/src/{agent,app,compiler,manager,misc}/*.erl
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/wx-*/src/gen/*.erl
find $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ -maxdepth 2 -type d -name src -empty -delete

# remove C and Java sources
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/asn1-*/c_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/erl_interface-*/src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ic-*/c_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ic-*/java_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/jinterface-*/java_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/odbc-*/c_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/tools-*/c_src

# remove empty or intermediate files and directories
rm -r $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/doc
rm -r $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/man
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/cosEvent-*/info
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/cosEventDomain-*/info
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/crypto-*/priv/obj
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/hipe-*/vsn.mk
rm -r $RPM_BUILD_ROOT%{_libdir}/erlang/lib/odbc-*/priv/obj
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ssl-*/priv/obj
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/misc

# fix permissions for asn1 library
chmod 755 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/asn1-*/priv/lib/asn1_erl_drv.so

# fix permissions for megaco library
chmod 755 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/megaco-*/priv/lib/megaco_flex_scanner_drv.so
chmod 755 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/megaco-*/priv/lib/megaco_flex_scanner_drv_mt.so

# fix permissons for wx library
chmod 755 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/wx-*/priv/*/wxe_driver.so

# Install RPM related files
install -D -p -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_libdir}/rpm/erlang-find-provides.escript
install -D -p -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/rpm/erlang-find-provides.sh
install -D -p -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_libdir}/rpm/erlang-find-requires.escript
install -D -p -m 0755 %{SOURCE6} $RPM_BUILD_ROOT%{_libdir}/rpm/erlang-find-requires.sh
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.erlang


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS EPLICENCE README.md
%{_bindir}/*
%{_libdir}/erlang

# RPM stuff
%{_sysconfdir}/rpm/macros.erlang
%{_libdir}/rpm/erlang-find-provides.escript
%{_libdir}/rpm/erlang-find-provides.sh
%{_libdir}/rpm/erlang-find-requires.escript
%{_libdir}/rpm/erlang-find-requires.sh


%files doc
%defattr(-,root,root)
%doc erlang_doc/*


%post
%{_libdir}/erlang/Install -minimal %{_libdir}/erlang >/dev/null 2>/dev/null


%changelog
* Fri Mar 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.3
- Added rpm-related stuff for auto-generating erlang dependencies in the future builds
- Since now *.yrl files are removed too.
- Removed unnecessary C and Java sources

* Fri Mar 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.2
- Do not remove all files from %%{_libdir}/erlang/lib/*/src - keep
  *.[yh]rl intact
- Fix permissions for megaco *.so objects
- Fix permissions for asn1 *.so objects

* Sat Feb 13 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.1
- New release R13B-04
- Since now we're using %%configure instead of ./configure
- Removed no longer needed fix for newer glibc version
- Dropped %%patch3 (applied upstream)
- Rebased patches
- Added BR fop for rebuilding of docs
- Use system-wide zlib instead of shipped one
- Dropped BR gd-devel
- Removed unneeded sources (should be fixed upstream)
- Fixed permission for wx driver (should be fixed upstream)

* Thu Oct 22 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - R13B-02-1
- Update to R13B-02 (patched for what's released as 02-1 by upstream)

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - R13B-01.2
- rebuilt with new openssl

* Mon Aug 10 2009 Gerard Milmeister <gemi@bluewin.ch> - R13B-01.1
- update to R13B01

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R12B-6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Debarshi Ray <rishi@fedoraproject.org> R12B-5.7
- Updated rpath patch.
- Fixed configure to respect $RPM_OPT_FLAGS.

* Sun Mar  1 2009 Gerard Milmeister <gemi@bluewin.ch> - R12B-5.6
- new release R12B-5
- link escript and dialyzer to %{_bindir}

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R12B-5.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Dennis Gilmore <dennis@ausil.us> - R12B-4.5
- fix sparc arches to compile

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - R12B-4.4
- rebuild with new openssl

* Sat Oct 25 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-4.1
- new release R12B-4

* Fri Sep  5 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-3.3
- fixed sslrpath patch

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - R12B-3.2
- fix license tag

* Sun Jul  6 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-3.1
- new release R12B-3

* Thu Mar 27 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-1.1
- new release R12B-1

* Sat Feb 23 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-0.3
- disable strict aliasing optimization

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - R12B-0.2
- Autorebuild for GCC 4.3

* Sat Dec  8 2007 Gerard Milmeister <gemi@bluewin.ch> - R12B-0.1
- new release R12B-0

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - R11B-6
 - Rebuild for deps

* Sun Aug 19 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.3
- fix some permissions

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.2
- enable dynamic linking for ssl

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.1
- new release R11B-5

* Sat Mar 24 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - R11B-2.4
- Require java-1.5.0-gcj-devel for build.

* Sun Dec 31 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.3
- remove buildroot from installed files

* Sat Dec 30 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.2
- added patch for compiling with glibc 2.5

* Sat Dec 30 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.1
- new version R11B-2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.3
- Rebuild for FE6

* Wed Jul  5 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.2
- add BR m4

* Thu May 18 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.1
- new version R11B-0

* Wed May  3 2006 Gerard Milmeister <gemi@bluewin.ch> - R10B-10.3
- added patch for run_erl by Knut-Håvard Aksnes

* Mon Mar 13 2006 Gerard Milmeister <gemi@bluewin.ch> - R10B-10.1
- new version R10B-10

* Thu Dec 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-9.1
- New Version R10B-9

* Sat Oct 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-8.2
- updated rpath patch

* Sat Oct 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-8.1
- New Version R10B-8

* Sat Oct  1 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.4
- Added tk-devel and tcl-devel to buildreq
- Added tk to req

* Tue Sep  6 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.3
- Remove perl BuildRequires

* Tue Aug 30 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.2
- change /usr/lib to %%{_libdir}
- redirect output in %%post to /dev/null
- add unixODBC-devel to BuildRequires
- split doc off to erlang-doc package

* Sat Jun 25 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.1
- New Version R10B-6

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-3.1
- New Version R10B-3

* Mon Dec 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:R10B-2-0.fdr.1
- New Version R10B-2

* Wed Oct  6 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:R10B-0.fdr.1
- New Version R10B

* Thu Oct 16 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:R9B-1.fdr.1
- First Fedora release
