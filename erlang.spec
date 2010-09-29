%global upstream_ver R14B
# Do NOT change %%{upstream_rel} unless UPSTREAM has actually changed it!
%global upstream_rel 0

%bcond_without doc

%global n_uvr %{name}-%{upstream_ver}-%{upstream_rel}

Name:		erlang
Version:	%{upstream_ver}
Release:	%{upstream_rel}.1%{?dist}.1
Summary:	General-purpose programming language and runtime environment

Group:		Development/Languages
License:	ERPL
URL:		http://www.erlang.org
Source0:	http://www.erlang.org/download/otp_src_%{upstream_ver}.tar.gz
Source3:	erlang-find-provides.escript
Source4:	erlang-find-provides.sh
Source5:	erlang-find-requires.escript
Source6:	erlang-find-requires.sh
Source7:	macros.erlang
# Fedora-specific
Patch1:		otp-0001-Do-not-format-man-pages-and-do-not-install-miscellan.patch
# Fedora-specific
Patch2:		otp-0002-Remove-rpath.patch
# Fedora-specific
Patch4:		otp-0004-Fix-for-dlopening-libGL-and-libGLU.patch
# Fedora-specific
Patch5:		otp-0005-Do-not-install-C-sources.patch
# Fedora-specific
Patch6:		otp-0006-Do-not-install-Java-sources.patch
# Fedora-specific
Patch7:		otp-0007-Do-not-install-info-files-they-are-almost-empty-and-.patch
# Fedora-specific
Patch8:		otp-0008-Do-not-install-nteventlog-and-related-doc-files-on-n.patch
# Fedora-specific
Patch9:		otp-0009-Do-not-install-.bat-files-on-non-win32-machines.patch
# Fedora-specific
Patch10:	otp-0010-Do-not-install-VxWorks-specific-docs.patch
# Fedora-specific
Patch11:	otp-0011-Do-not-install-erlang-sources.patch
# Will be proposed for inclusion into upstream
Patch12:	otp-0012-Fix-installation-of-example-file.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	flex
BuildRequires:	m4
BuildRequires:	fop
BuildRequires:	libxslt
# Required for building docs (escript)
BuildRequires:	erlang

BuildRequires:	emacs
BuildRequires:	xemacs
BuildRequires:	emacs-el
BuildRequires:	xemacs-packages-extra-el

Requires: erlang-appmon = %{version}-%{release}
Requires: erlang-asn1 = %{version}-%{release}
Requires: erlang-common_test = %{version}-%{release}
Requires: erlang-compiler = %{version}-%{release}
Requires: erlang-cosEvent = %{version}-%{release}
Requires: erlang-cosEventDomain = %{version}-%{release}
Requires: erlang-cosFileTransfer = %{version}-%{release}
Requires: erlang-cosNotification = %{version}-%{release}
Requires: erlang-cosProperty = %{version}-%{release}
Requires: erlang-cosTime = %{version}-%{release}
Requires: erlang-cosTransactions = %{version}-%{release}
Requires: erlang-crypto = %{version}-%{release}
Requires: erlang-debugger = %{version}-%{release}
Requires: erlang-dialyzer = %{version}-%{release}
Requires: erlang-docbuilder = %{version}-%{release}
Requires: erlang-edoc = %{version}-%{release}
Requires: erlang-erl_docgen = %{version}-%{release}
Requires: erlang-erl_interface = %{version}-%{release}
Requires: erlang-erts = %{version}-%{release}
Requires: erlang-et = %{version}-%{release}
Requires: erlang-eunit = %{version}-%{release}
Requires: erlang-examples = %{version}-%{release}
Requires: erlang-gs = %{version}-%{release}
Requires: erlang-hipe = %{version}-%{release}
Requires: erlang-ic = %{version}-%{release}
Requires: erlang-inets = %{version}-%{release}
Requires: erlang-inviso = %{version}-%{release}
Requires: erlang-jinterface = %{version}-%{release}
Requires: erlang-kernel = %{version}-%{release}
Requires: erlang-megaco = %{version}-%{release}
Requires: erlang-mnesia = %{version}-%{release}
Requires: erlang-observer = %{version}-%{release}
Requires: erlang-odbc = %{version}-%{release}
Requires: erlang-orber = %{version}-%{release}
Requires: erlang-os_mon = %{version}-%{release}
Requires: erlang-otp_mibs = %{version}-%{release}
Requires: erlang-parsetools = %{version}-%{release}
Requires: erlang-percept = %{version}-%{release}
Requires: erlang-pman = %{version}-%{release}
Requires: erlang-public_key = %{version}-%{release}
Requires: erlang-reltool = %{version}-%{release}
Requires: erlang-rpm-macros = %{version}-%{release}
Requires: erlang-runtime_tools = %{version}-%{release}
Requires: erlang-sasl = %{version}-%{release}
Requires: erlang-snmp = %{version}-%{release}
Requires: erlang-ssh = %{version}-%{release}
Requires: erlang-ssl = %{version}-%{release}
Requires: erlang-stdlib = %{version}-%{release}
Requires: erlang-syntax_tools = %{version}-%{release}
Requires: erlang-test_server = %{version}-%{release}
Requires: erlang-toolbar = %{version}-%{release}
Requires: erlang-tools = %{version}-%{release}
Requires: erlang-tv = %{version}-%{release}
Requires: erlang-typer = %{version}-%{release}
Requires: erlang-webtool = %{version}-%{release}
Requires: erlang-wx = %{version}-%{release}
Requires: erlang-xmerl = %{version}-%{release}

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package appmon
Summary:	A utility used to supervise Applications executing on several Erlang nodes
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-gs = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description appmon
A utility used to supervise Applications executing on several Erlang nodes.

%package asn1
Summary:	Provides support for Abstract Syntax Notation One
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-syntax_tools = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description asn1
Provides support for Abstract Syntax Notation One.

%package common_test
Summary:	A portable framework for automatic testing
Group:		Development/Languages
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-crypto = %{version}-%{release}
Requires: %{name}-debugger = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-snmp = %{version}-%{release}
Requires: %{name}-ssh = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-test_server = %{version}-%{release}
Requires: %{name}-tools = %{version}-%{release}
Requires: %{name}-webtool = %{version}-%{release}
Requires: %{name}-xmerl = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description common_test
A portable framework for automatic testing.

%package compiler
Summary:	A byte code compiler for Erlang which produces highly compact code
Group:		Development/Languages
Requires: %{name}-crypto = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-hipe = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description compiler
A byte code compiler for Erlang which produces highly compact code.

%package cosEvent
Summary:	Orber OMG Event Service
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-orber = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosEvent
Orber OMG Event Service.

%package cosEventDomain
Summary:	Orber OMG Event Domain Service
Group:		Development/Languages
Requires: %{name}-cosNotification = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-orber = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosEventDomain
Orber OMG Event Domain Service.

%package cosFileTransfer
Summary:	Orber OMG File Transfer Service
Group:		Development/Languages
Requires: %{name}-cosProperty = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-orber = %{version}-%{release}
Requires: %{name}-ssl = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosFileTransfer
Orber OMG File Transfer Service.

%package cosNotification
Summary:	Orber OMG Notification Service
Group:		Development/Languages
Requires: %{name}-cosEvent = %{version}-%{release}
Requires: %{name}-cosTime = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-orber = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosNotification
Orber OMG Notification Service.

%package cosProperty
Summary:	Orber OMG Property Service
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-mnesia = %{version}-%{release}
Requires: %{name}-orber = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosProperty
Orber OMG Property Service.

%package cosTime
Summary:	Orber OMG Timer and TimerEvent Service
Group:		Development/Languages
Requires: %{name}-cosEvent = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-orber = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosTime
Orber OMG Timer and TimerEvent Service.

%package cosTransactions
Summary:	Orber OMG Transaction Service
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-orber = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5
Obsoletes:	%{name}-cosTransaction < R13B-04.7

%description cosTransactions
Orber OMG Transaction Service.

%package crypto
Summary:	Cryptographical support
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description crypto
Cryptographical support.

%package debugger
Summary:	A debugger for debugging and testing of Erlang programs
Group:		Development/Languages
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-gs = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-wx = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description debugger
A debugger for debugging and testing of Erlang programs.

%package dialyzer
Summary:	A DIscrepany AnaLYZer for ERlang programs
Group:		Development/Languages
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-gs = %{version}-%{release}
Requires: %{name}-hipe = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-syntax_tools = %{version}-%{release}
Requires: %{name}-wx = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description dialyzer
A DIscrepany AnaLYZer for ERlang programs.

%package doc
Summary:	Erlang documentation
Group:		Development/Languages
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-doc < R13B-04.4

%description doc
Documentation for Erlang.

%package docbuilder
Summary:	Tool for generating HTML documentation for applications
Group:		Development/Languages
Requires: %{name}-edoc = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-xmerl = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description docbuilder
Tool for generating HTML documentation for applications.

%package edoc
Summary:	A utility used to generate documentation out of tags in source files
Group:		Development/Languages
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-syntax_tools = %{version}-%{release}
Requires: %{name}-xmerl = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description edoc
A utility used to generate documentation out of tags in source files.

%package erl_docgen
Summary:	A utility used to generate erlang HTML documentation
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description erl_docgen
A utility used to generate erlang HTML documentation.

%package erl_interface
Summary:	Low level interface to C
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description erl_interface
Low level interface to C.

%package erts
Summary:	Functionality necessary to run the Erlang System itself
Group:		Development/Languages
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description erts
Functionality necessary to run the Erlang System itself.

%package et
Summary:	An event tracer for Erlang programs
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-gs = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-wx = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description et
An event tracer for Erlang programs.

%package eunit
Summary:	Support for unit testing
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description eunit
Support for unit testing.

%package examples
Summary:	Examples for some Erlang modules
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description examples
Examples for some Erlang modules.

%package gs
Summary:	A library for Tcl/Tk support in Erlang
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
Requires:	tk
Obsoletes:	%{name} < R13B-04.5

%description gs
A Graphics System used to write platform independent user interfaces.

%package hipe
Summary:	High Performance Erlang
Group:		Development/Languages
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-syntax_tools = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description hipe
High Performance Erlang.

%package ic
Summary:	IDL compiler
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description ic
IDL compiler.

%package inets
Summary:	A set of services such as a Web server and a ftp client etc
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-mnesia = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-ssl = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description inets
A set of services such as a Web server and a ftp client etc.

%package inviso
Summary:	A trace tool for both development and delivered systems
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description inviso
A trace tool for both development and delivered systems.

%package jinterface
Summary:	A library for accessing Java from Erlang
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5
BuildRequires:	java-1.6.0-openjdk-devel

%description jinterface
Low level interface to Java.

%package kernel
Summary:	Main erlang library
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description kernel
Main erlang library.

%package megaco
Summary:	Megaco/H.248 support library
Group:		Development/Languages
Requires: %{name}-asn1 = %{version}-%{release}
Requires: %{name}-debugger = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-et = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description megaco
Megaco/H.248 is a protocol for control of elements in a physically
decomposed multimedia gateway, enabling separation of call control
from media conversion.

%package mnesia
Summary:	A heavy duty real-time distributed database
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description mnesia
A heavy duty real-time distributed database.

%package observer
Summary:	A set of tools for tracing and investigation of distributed systems
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-et = %{version}-%{release}
Requires: %{name}-gs = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-webtool = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description observer
A set of tools for tracing and investigation of distributed systems.

%package odbc
Summary:	A library for unixODBC support in Erlang
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5
BuildRequires:	unixODBC-devel

%description odbc
An interface to relational SQL-databases built on ODBC (Open Database
Connectivity).

%package orber
Summary:	A CORBA Object Request Broker
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-mnesia = %{version}-%{release}
Requires: %{name}-ssl = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description orber
A CORBA Object Request Broker.

%package os_mon
Summary:	A monitor which allows inspection of the underlying operating system
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-mnesia = %{version}-%{release}
Requires: %{name}-otp_mibs = %{version}-%{release}
Requires: %{name}-sasl = %{version}-%{release}
Requires: %{name}-snmp = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description os_mon
A monitor which allows inspection of the underlying operating system.

%package otp_mibs
Summary:	SNMP management information base for Erlang/OTP nodes
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-mnesia = %{version}-%{release}
Requires: %{name}-snmp = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description otp_mibs
SNMP management information base for Erlang/OTP nodes.

%package parsetools
Summary:	A set of parsing and lexical analysis tools
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description parsetools
A set of parsing and lexical analysis tools.

%package percept
Summary:	A concurrency profiler tool
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description percept
A concurrency profiler tool.

%package pman
Summary:	A graphical process manager used to inspect Erlang processes
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-gs = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description pman
A graphical process manager used to inspect Erlang processes.

%package public_key
Summary:	API to public key infrastructure
Group:		Development/Languages
Requires: %{name}-crypto = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description public_key
API to public key infrastructure.

%package reltool
Summary:	A release management tool
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-sasl = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-syntax_tools = %{version}-%{release}
Requires: %{name}-tools = %{version}-%{release}
Requires: %{name}-wx = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description reltool
Reltool is a release management tool. It analyses a given
Erlang/OTP installation and determines various dependencies
between applications. The graphical frontend depicts the
dependencies and enables interactive customization of a
target system. The backend provides a batch interface
for generation of customized target systems.

%package rpm-macros
Summary:	Necessary macros for building Erlang
Group:		Development/Languages
Obsoletes:	%{name} < R13B-04.5

%description rpm-macros
Necessary macros for building Erlang.

%package runtime_tools
Summary:	A set of tools to include in a production system
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description runtime_tools
A set of tools to include in a production system.

%package sasl
Summary:	The System Architecture Support Libraries
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-tools = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description sasl
The System Architecture Support Libraries is a set of tools for
release upgrades and alarm handling etc.

%package snmp
Summary:	Simple Network Management Protocol (SNMP) support
Group:		Development/Languages
Requires: %{name}-crypto = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-mnesia = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description snmp
Simple Network Management Protocol (SNMP) support including a
MIB compiler and tools for creating SNMP agents.

%package ssh
Summary:	Secure Shell application with sftp and ssh support
Group:		Development/Languages
Requires: %{name}-crypto = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-public_key = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description ssh
Secure Shell application with sftp and ssh support.

%package ssl
Summary:	Secure Socket Layer support
Group:		Development/Languages
Requires: %{name}-crypto = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-public_key = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description ssl
Secure Socket Layer support.

%package stdlib
Summary:	The Erlang standard libraries
Group:		Development/Languages
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-crypto = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description stdlib
The Erlang standard libraries.

%package syntax_tools
Summary:	A set of tools for dealing with erlang sources
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description syntax_tools
A utility used to handle abstract Erlang syntax trees,
reading source files differently, pretty-printing syntax trees.

%package test_server
Summary:	The OTP Test Server
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-observer = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-sasl = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-tools = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description test_server
The OTP Test Server.

%package toolbar
Summary:	A tool bar simplifying access to the Erlang tools
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-gs = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description toolbar
A tool bar simplifying access to the Erlang tools.

%package tools
Summary:	A set of programming tools including a coverage analyzer etc
Group:		Development/Languages
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-runtime_tools = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires: %{name}-webtool = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5
Provides:	emacs-common-erlang = %{version}-%{release}

%description tools
A set of programming tools including a coverage analyzer etc.

%package tv
Summary:	An ETS and MNESIA graphical table visualizer
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-gs = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-mnesia = %{version}-%{release}
Requires: %{name}-pman = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description tv
An ETS and MNESIA graphical table visualizer.

%package typer
Summary:	TYPe annotator for ERlang programs
Group:		Development/Languages
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-dialyzer = %{version}-%{release}
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-hipe = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description typer
TYPe annotator for ERlang programs.

%package webtool
Summary:	A tool that simplifying the use of web based Erlang tools
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-inets = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-observer = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description webtool
A tool that simplifying the use of web based Erlang tools.

%package wx
Summary:	A library for wxWidgets support in Erlang
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Requires:	mesa-libGL
Requires:	mesa-libGLU
Obsoletes:	%{name} < R13B-04.5
BuildRequires:	wxGTK-devel

%description wx
A Graphics System used to write platform independent user interfaces.

%package xmerl
Summary:	Provides support for XML 1.0
Group:		Development/Languages
Requires: %{name}-erts = %{version}-%{release}
Requires: %{name}-kernel = %{version}-%{release}
Requires: %{name}-stdlib = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description xmerl
Provides support for XML 1.0.

%package -n emacs-erlang
Summary:	Compiled elisp files for erlang-mode under GNU Emacs
Requires:	emacs-common-erlang = %{version}-%{release}
Requires:	emacs(bin) >= %{_emacs_version}
Group:		Applications/Editors
BuildArch:	noarch

%description -n emacs-erlang
Erlang mode for GNU Emacs.

%package -n emacs-erlang-el
Summary:	Elisp source files for erlang-mode under GNU Emacs
Requires:	emacs-erlang = %{version}-%{release}
Group:		Applications/Editors
BuildArch:	noarch

%description -n emacs-erlang-el
Erlang mode for GNU Emacs (source lisp files).

%package -n xemacs-erlang
Summary:	Compiled elisp files for erlang-mode under XEmacs
Requires:	emacs-common-erlang = %{version}-%{release}
Group:		Applications/Editors
BuildArch:	noarch
Requires:	xemacs(bin) >= %{_xemacs_version}

%description -n xemacs-erlang
Erlang mode for XEmacs.

%package -n xemacs-erlang-el
Summary:	Elisp source files for erlang-mode under XEmacs
Requires:	xemacs-erlang = %{version}-%{release}
Group:		Applications/Editors
BuildArch:	noarch

%description -n xemacs-erlang-el
Erlang mode for XEmacs (source lisp files).

%prep
%setup -q -n otp_src_%{upstream_ver}
%patch1 -p1 -b .do_not_format_manpages
%patch2 -p1 -b .rpath
%patch4 -p1 -b .dlopen_opengl_libs
%patch5 -p1 -b .no_c_sources
%patch6 -p1 -b .no_java_sources
%patch7 -p1 -b .no_info_files
%patch8 -p1 -b .no_win32_nteventlog
%patch9 -p1 -b .no_win32_bat_files
%patch10 -p1 -b .no_vxworks_specific
%patch11 -p1 -b .no_erlang_sources
%patch12 -p1 -b .install_example_file_properly
# remove shipped zlib sources
rm -f erts/emulator/zlib/*.[ch]

# Fix 664 file mode
chmod 644 lib/kernel/examples/uds_dist/c_src/Makefile
chmod 644 lib/kernel/examples/uds_dist/src/Makefile
chmod 644 lib/ssl/examples/certs/Makefile
chmod 644 lib/ssl/examples/src/Makefile

# Remove old txt files
rm -f lib/ssl/examples/certs/etc/otpCA/index.txt.old
rm -f lib/ssl/examples/certs/etc/erlangCA/index.txt.old


%build
%ifarch sparcv9 sparc64
CFLAGS="$RPM_OPT_FLAGS -mcpu=ultrasparc -fno-strict-aliasing" %configure --enable-shared-zlib
%else
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %configure --enable-shared-zlib
%endif

# GNU Emacs/XEmacs related stuff
erlang_tools_vsn="$(sed -n 's/TOOLS_VSN = //p' lib/tools/vsn.mk)"

# GNU Emacs related stuff
cat > emacs-erlang-init.el << EOF
(setq load-path (cons "%{_emacs_sitelispdir}/erlang" load-path))
(setq erlang-root-dir "%{_libdir}/erlang")
(setq exec-path (cons "%{_libdir}/erlang/bin" exec-path))
(require 'erlang-start)
EOF
mkdir emacs-erlang
cp lib/tools/emacs/*.el emacs-erlang/
pushd emacs-erlang
%{_emacs_bytecompile} *.el
popd

# XEmacs related stuff
cat > xemacs-erlang-init.el << EOF
(setq load-path (cons "%{_xemacs_sitelispdir}/erlang" load-path))
(setq erlang-root-dir "%{_libdir}/erlang")
(setq exec-path (cons "%{_libdir}/erlang/bin" exec-path))
(require 'erlang-start)
EOF
mkdir xemacs-erlang
cp lib/tools/emacs/*.el xemacs-erlang/
rm -f xemacs-erlang/erlang-flymake.el
pushd xemacs-erlang
%{_xemacs_bytecompile} *.el
popd

make
%if %{with doc}
make docs
%endif


%install
rm -rf $RPM_BUILD_ROOT

# GNU Emacs/XEmacs related stuff
erlang_tools_vsn="$(sed -n 's/TOOLS_VSN = //p' lib/tools/vsn.mk)"

# GNU Emacs related stuff
install -m 0755 -d "$RPM_BUILD_ROOT%{_emacs_sitestartdir}"
install -m 0755 -d "$RPM_BUILD_ROOT%{_emacs_sitelispdir}/erlang"
install -m 0644 emacs-erlang-init.el "$RPM_BUILD_ROOT%{_emacs_sitestartdir}/erlang-init.el"
for f in lib/tools/emacs/{README,*.el}; do
	b="$(basename "$f")";
	ln -s "%{_libdir}/erlang/lib/tools-${erlang_tools_vsn}/emacs/$b" \
		"$RPM_BUILD_ROOT%{_emacs_sitelispdir}/erlang/"
done
install -m 0644 emacs-erlang/*.elc "$RPM_BUILD_ROOT%{_emacs_sitelispdir}/erlang/"

# XEmacs related stuff
install -m 0755 -d "$RPM_BUILD_ROOT%{_xemacs_sitestartdir}"
install -m 0755 -d "$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/erlang"
install -m 0644 xemacs-erlang-init.el "$RPM_BUILD_ROOT%{_xemacs_sitestartdir}/erlang-init.el"
for f in lib/tools/emacs/{README,*.el}; do
	b="$(basename "$f")";
	ln -s "%{_libdir}/erlang/lib/tools-${erlang_tools_vsn}/emacs/$b" \
		"$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/erlang/"
done
rm -f "$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/erlang/erlang-flymake.el"
install -m 0644 xemacs-erlang/*.elc "$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/erlang/"

make DESTDIR=$RPM_BUILD_ROOT install
%if %{with doc}
make DESTDIR=$RPM_BUILD_ROOT install-docs
%endif

# fix 0775 permission on some directories
find $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ssl-*/examples/ -type d -perm 0775 | xargs chmod 755
find $RPM_BUILD_ROOT%{_libdir}/erlang/lib/kernel-*/examples/uds_dist -type d -perm 0775 | xargs chmod 755
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/erlang/bin

# Relocate doc-files into the proper directory
%if %{with doc}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{n_uvr}/lib
pushd .
cd $RPM_BUILD_ROOT%{_libdir}/erlang
mv -v doc $RPM_BUILD_ROOT%{_docdir}/%{n_uvr}
for i in erts-* ; do mv -v $i/doc $RPM_BUILD_ROOT%{_docdir}/%{n_uvr}/$i ; done
cd $RPM_BUILD_ROOT%{_libdir}/erlang/lib
for i in * ; do mv -v $i/doc $RPM_BUILD_ROOT%{_docdir}/%{n_uvr}/lib/$i || true ; done
popd
cp -av AUTHORS EPLICENCE README.md $RPM_BUILD_ROOT%{_docdir}/%{n_uvr}
mv -v $RPM_BUILD_ROOT%{_libdir}/erlang/PR.template $RPM_BUILD_ROOT%{_docdir}/%{n_uvr}
mv -v $RPM_BUILD_ROOT%{_libdir}/erlang/README $RPM_BUILD_ROOT%{_docdir}/%{n_uvr}
mv -v $RPM_BUILD_ROOT%{_libdir}/erlang/COPYRIGHT $RPM_BUILD_ROOT%{_docdir}/%{n_uvr}
%endif

# Win32-specific man-pages
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man1/erlsrv.*
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man1/werl.*
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man3/win32reg.*

# remove empty directory
rm -r $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/man

# Install RPM related files
install -D -p -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_rpmconfigdir}/erlang-find-provides.escript
install -D -p -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{_rpmconfigdir}/erlang-find-provides.sh
install -D -p -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_rpmconfigdir}/erlang-find-requires.escript
install -D -p -m 0755 %{SOURCE6} $RPM_BUILD_ROOT%{_rpmconfigdir}/erlang-find-requires.sh
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.erlang

# remove outdated script
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/Install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%if %{with doc}
%dir %{_docdir}/%{n_uvr}/
%doc %{_docdir}/%{n_uvr}/AUTHORS
%doc %{_docdir}/%{n_uvr}/COPYRIGHT
%doc %{_docdir}/%{n_uvr}/EPLICENCE
%doc %{_docdir}/%{n_uvr}/PR.template
%doc %{_docdir}/%{n_uvr}/README
%doc %{_docdir}/%{n_uvr}/README.md
%endif

%files appmon
%defattr(-,root,root)
%{_libdir}/erlang/lib/appmon-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/appmon.*
%endif

%files asn1
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/asn1-*/
%{_libdir}/erlang/lib/asn1-*/ebin
%{_libdir}/erlang/lib/asn1-*/priv
%{_libdir}/erlang/lib/asn1-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/asn1ct.*
%{_libdir}/erlang/man/man3/asn1rt.*
%endif

%files common_test
%defattr(-,root,root)
%{_libdir}/erlang/lib/common_test-*/
%if %{with doc}
%{_libdir}/erlang/man/man1/run_test.*
%{_libdir}/erlang/man/man3/ct.*
%{_libdir}/erlang/man/man3/ct_cover.*
%{_libdir}/erlang/man/man3/ct_ftp.*
%{_libdir}/erlang/man/man3/ct_master.*
%{_libdir}/erlang/man/man3/ct_rpc.*
%{_libdir}/erlang/man/man3/ct_slave.*
%{_libdir}/erlang/man/man3/ct_snmp.*
%{_libdir}/erlang/man/man3/ct_ssh.*
%{_libdir}/erlang/man/man3/ct_telnet.*
%{_libdir}/erlang/man/man3/unix_telnet.*
%{_libdir}/erlang/man/man6/common_test.*
%endif

%files compiler
%defattr(-,root,root)
%{_libdir}/erlang/lib/compiler-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/compile.*
%endif

%files cosEvent
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosEvent-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/cosEventApp.*
%{_libdir}/erlang/man/man3/CosEventChannelAdmin.*
%{_libdir}/erlang/man/man3/CosEventChannelAdmin_ConsumerAdmin.*
%{_libdir}/erlang/man/man3/CosEventChannelAdmin_EventChannel.*
%{_libdir}/erlang/man/man3/CosEventChannelAdmin_ProxyPullConsumer.*
%{_libdir}/erlang/man/man3/CosEventChannelAdmin_ProxyPullSupplier.*
%{_libdir}/erlang/man/man3/CosEventChannelAdmin_ProxyPushConsumer.*
%{_libdir}/erlang/man/man3/CosEventChannelAdmin_ProxyPushSupplier.*
%{_libdir}/erlang/man/man3/CosEventChannelAdmin_SupplierAdmin.*
%endif

%files cosEventDomain
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosEventDomain-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/CosEventDomainAdmin.*
%{_libdir}/erlang/man/man3/CosEventDomainAdmin_EventDomain.*
%{_libdir}/erlang/man/man3/CosEventDomainAdmin_EventDomainFactory.*
%{_libdir}/erlang/man/man3/cosEventDomainApp.*
%endif

%files cosFileTransfer
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosFileTransfer-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/cosFileTransferApp.*
%{_libdir}/erlang/man/man3/CosFileTransfer_Directory.*
%{_libdir}/erlang/man/man3/CosFileTransfer_File.*
%{_libdir}/erlang/man/man3/CosFileTransfer_FileIterator.*
%{_libdir}/erlang/man/man3/CosFileTransfer_FileTransferSession.*
%{_libdir}/erlang/man/man3/CosFileTransfer_VirtualFileSystem.*
%endif

%files cosNotification
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosNotification-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/CosNotification.*
%{_libdir}/erlang/man/man3/CosNotification_AdminPropertiesAdmin.*
%{_libdir}/erlang/man/man3/cosNotificationApp.*
%{_libdir}/erlang/man/man3/CosNotification_QoSAdmin.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_ConsumerAdmin.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_EventChannel.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_EventChannelFactory.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_ProxyConsumer.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_ProxyPullConsumer.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_ProxyPullSupplier.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_ProxyPushConsumer.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_ProxyPushSupplier.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_ProxySupplier.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_SequenceProxyPullConsumer.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_SequenceProxyPullSupplier.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_SequenceProxyPushConsumer.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_SequenceProxyPushSupplier.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_StructuredProxyPullConsumer.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_StructuredProxyPullSupplier.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_StructuredProxyPushConsumer.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_StructuredProxyPushSupplier.*
%{_libdir}/erlang/man/man3/CosNotifyChannelAdmin_SupplierAdmin.*
%{_libdir}/erlang/man/man3/CosNotifyComm_NotifyPublish.*
%{_libdir}/erlang/man/man3/CosNotifyComm_NotifySubscribe.*
%{_libdir}/erlang/man/man3/CosNotifyFilter_Filter.*
%{_libdir}/erlang/man/man3/CosNotifyFilter_FilterAdmin.*
%{_libdir}/erlang/man/man3/CosNotifyFilter_FilterFactory.*
%{_libdir}/erlang/man/man3/CosNotifyFilter_MappingFilter.*
%endif

%files cosProperty
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosProperty-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/cosProperty.*
%{_libdir}/erlang/man/man3/CosPropertyService_PropertiesIterator.*
%{_libdir}/erlang/man/man3/CosPropertyService_PropertyNamesIterator.*
%{_libdir}/erlang/man/man3/CosPropertyService_PropertySet.*
%{_libdir}/erlang/man/man3/CosPropertyService_PropertySetDef.*
%{_libdir}/erlang/man/man3/CosPropertyService_PropertySetDefFactory.*
%{_libdir}/erlang/man/man3/CosPropertyService_PropertySetFactory.*
%endif

%files cosTime
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosTime-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/cosTime.*
%{_libdir}/erlang/man/man3/CosTimerEvent_TimerEventHandler.*
%{_libdir}/erlang/man/man3/CosTimerEvent_TimerEventService.*
%{_libdir}/erlang/man/man3/CosTime_TimeService.*
%{_libdir}/erlang/man/man3/CosTime_TIO.*
%{_libdir}/erlang/man/man3/CosTime_UTO.*
%endif

%files cosTransactions
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosTransactions-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/cosTransactions.*
%{_libdir}/erlang/man/man3/CosTransactions_Control.*
%{_libdir}/erlang/man/man3/CosTransactions_Coordinator.*
%{_libdir}/erlang/man/man3/CosTransactions_RecoveryCoordinator.*
%{_libdir}/erlang/man/man3/CosTransactions_Resource.*
%{_libdir}/erlang/man/man3/CosTransactions_SubtransactionAwareResource.*
%{_libdir}/erlang/man/man3/CosTransactions_Terminator.*
%{_libdir}/erlang/man/man3/CosTransactions_TransactionFactory.*
%endif

%files crypto
%defattr(-,root,root)
%{_libdir}/erlang/lib/crypto-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/crypto.*
%{_libdir}/erlang/man/man6/crypto.*
%endif

%files debugger
%defattr(-,root,root)
%{_libdir}/erlang/lib/debugger-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/debugger.*
%{_libdir}/erlang/man/man3/i.*
%{_libdir}/erlang/man/man3/int.*
%endif

%files dialyzer
%defattr(-,root,root)
%{_bindir}/dialyzer
%{_libdir}/erlang/bin/dialyzer
%{_libdir}/erlang/erts-*/bin/dialyzer
%{_libdir}/erlang/lib/dialyzer-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/dialyzer.*
%endif

%files doc
%defattr(-,root,root)
%if %{with doc}
%doc %{_docdir}/%{n_uvr}/doc
%doc %{_docdir}/%{n_uvr}/erts-*/
%doc %{_docdir}/%{n_uvr}/lib/
%endif


%files docbuilder
%defattr(-,root,root)
%{_libdir}/erlang/lib/docbuilder-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/docb_gen.*
%{_libdir}/erlang/man/man3/docb_transform.*
%{_libdir}/erlang/man/man3/docb_xml_check.*
%{_libdir}/erlang/man/man6/docbuilder.*
%endif

%files edoc
%defattr(-,root,root)
%{_libdir}/erlang/lib/edoc-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/edoc.*
%{_libdir}/erlang/man/man3/edoc_doclet.*
%{_libdir}/erlang/man/man3/edoc_extract.*
%{_libdir}/erlang/man/man3/edoc_layout.*
%{_libdir}/erlang/man/man3/edoc_lib.*
%{_libdir}/erlang/man/man3/edoc_run.*
%endif

%files erl_docgen
%defattr(-,root,root)
%{_libdir}/erlang/lib/erl_docgen-*/

%files erl_interface
%defattr(-,root,root)
%{_libdir}/erlang/lib/erl_interface-*/
%if %{with doc}
%{_libdir}/erlang/man/man1/erl_call.*
%{_libdir}/erlang/man/man3/ei.*
%{_libdir}/erlang/man/man3/ei_connect.*
%{_libdir}/erlang/man/man3/erl_connect.*
%{_libdir}/erlang/man/man3/erl_error.*
%{_libdir}/erlang/man/man3/erl_eterm.*
%{_libdir}/erlang/man/man3/erl_format.*
%{_libdir}/erlang/man/man3/erl_global.*
%{_libdir}/erlang/man/man3/erl_malloc.*
%{_libdir}/erlang/man/man3/erl_marshal.*
%{_libdir}/erlang/man/man3/registry.*
%endif

%files erts
%defattr(-,root,root)

# TODO these directories should be packaged separately
%dir %{_libdir}/erlang/
%dir %{_libdir}/erlang/bin/
%dir %{_libdir}/erlang/lib/
%if %{with doc}
%dir %{_libdir}/erlang/man/
%dir %{_libdir}/erlang/man/man1/
%dir %{_libdir}/erlang/man/man3/
%dir %{_libdir}/erlang/man/man4/
%dir %{_libdir}/erlang/man/man6/
%dir %{_libdir}/erlang/man/man7/
%endif
%dir %{_libdir}/erlang/releases/

%{_bindir}/epmd
%{_bindir}/erl
%{_bindir}/erlc
%{_bindir}/escript
%{_bindir}/run_erl
%{_bindir}/run_test
%{_bindir}/to_erl
%{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/bin/erl
%{_libdir}/erlang/bin/erlc
%{_libdir}/erlang/bin/escript
%{_libdir}/erlang/bin/run_erl
%{_libdir}/erlang/bin/run_test
%{_libdir}/erlang/bin/start
%{_libdir}/erlang/bin/start.boot
%{_libdir}/erlang/bin/start.script
%{_libdir}/erlang/bin/start_clean.boot
%{_libdir}/erlang/bin/start_erl
%{_libdir}/erlang/bin/start_sasl.boot
%{_libdir}/erlang/bin/to_erl
%dir %{_libdir}/erlang/erts-*/bin
%{_libdir}/erlang/erts-*/bin/beam
%{_libdir}/erlang/erts-*/bin/beam.smp
%{_libdir}/erlang/erts-*/bin/child_setup
%{_libdir}/erlang/erts-*/bin/dyn_erl
%{_libdir}/erlang/erts-*/bin/epmd
%{_libdir}/erlang/erts-*/bin/erl
%{_libdir}/erlang/erts-*/bin/erl.src
%{_libdir}/erlang/erts-*/bin/erlc
%{_libdir}/erlang/erts-*/bin/erlexec
%{_libdir}/erlang/erts-*/bin/escript
%{_libdir}/erlang/erts-*/bin/heart
%{_libdir}/erlang/erts-*/bin/inet_gethost
%{_libdir}/erlang/erts-*/bin/run_erl
%{_libdir}/erlang/erts-*/bin/run_test
%{_libdir}/erlang/erts-*/bin/start
%{_libdir}/erlang/erts-*/bin/start.src
%{_libdir}/erlang/erts-*/bin/start_erl.src
%{_libdir}/erlang/erts-*/bin/to_erl
%{_libdir}/erlang/erts-*/include
%{_libdir}/erlang/erts-*/lib
%{_libdir}/erlang/erts-*/src
%{_libdir}/erlang/lib/erts-*/
%if %{with doc}
%{_libdir}/erlang/man/man1/epmd.*
%{_libdir}/erlang/man/man1/erl.*
%{_libdir}/erlang/man/man1/erlc.*
%{_libdir}/erlang/man/man1/escript.*
%{_libdir}/erlang/man/man1/run_erl.*
%{_libdir}/erlang/man/man1/start.*
%{_libdir}/erlang/man/man1/start_erl.*
%{_libdir}/erlang/man/man3/driver_entry.*
%{_libdir}/erlang/man/man3/erl_driver.*
%{_libdir}/erlang/man/man3/erl_nif.*
%{_libdir}/erlang/man/man3/erl_prim_loader.*
%{_libdir}/erlang/man/man3/erlang.*
%{_libdir}/erlang/man/man3/erts_alloc.*
%{_libdir}/erlang/man/man3/init.*
%{_libdir}/erlang/man/man3/zlib.*
%endif
%{_libdir}/erlang/releases/*
%{_libdir}/erlang/usr/

%files et
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/et-*/
%{_libdir}/erlang/lib/et-*/ebin
%{_libdir}/erlang/lib/et-*/include
%{_libdir}/erlang/lib/et-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/et.*
%{_libdir}/erlang/man/man3/et_collector.*
%{_libdir}/erlang/man/man3/et_selector.*
%{_libdir}/erlang/man/man3/et_viewer.*
%endif

%files eunit
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/eunit-*/
%{_libdir}/erlang/lib/eunit-*/ebin
%{_libdir}/erlang/lib/eunit-*/include
%if %{with doc}
%{_libdir}/erlang/man/man3/eunit.*
%{_libdir}/erlang/man/man3/eunit_surefire.*
%endif

%files examples
%defattr(-,root,root)
%{_libdir}/erlang/lib/asn1-*/examples
%{_libdir}/erlang/lib/et-*/examples
%{_libdir}/erlang/lib/eunit-*/examples
%{_libdir}/erlang/lib/gs-*/examples
%{_libdir}/erlang/lib/ic-*/examples
%{_libdir}/erlang/lib/inets-*/examples
%{_libdir}/erlang/lib/kernel-*/examples
%{_libdir}/erlang/lib/megaco-*/examples
%{_libdir}/erlang/lib/mnesia-*/examples
%{_libdir}/erlang/lib/observer-*/examples
%{_libdir}/erlang/lib/orber-*/examples
%{_libdir}/erlang/lib/reltool-*/examples
%{_libdir}/erlang/lib/snmp-*/examples
%{_libdir}/erlang/lib/ssl-*/examples
%{_libdir}/erlang/lib/stdlib-*/examples
%{_libdir}/erlang/lib/syntax_tools-*/examples
%{_libdir}/erlang/lib/tools-*/examples
%{_libdir}/erlang/lib/wx-*/examples

%files gs
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/gs-*/
%{_libdir}/erlang/lib/gs-*/contribs
%{_libdir}/erlang/lib/gs-*/ebin
%{_libdir}/erlang/lib/gs-*/priv
%{_libdir}/erlang/lib/gs-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/gs.*
%endif

%files hipe
%defattr(-,root,root)
%{_libdir}/erlang/lib/hipe-*/

%files ic
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/ic-*/
%{_libdir}/erlang/lib/ic-*/ebin
%{_libdir}/erlang/lib/ic-*/include
%{_libdir}/erlang/lib/ic-*/priv
%{_libdir}/erlang/lib/ic-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/ic.*
%{_libdir}/erlang/man/man3/ic_clib.*
%{_libdir}/erlang/man/man3/ic_c_protocol.*
%endif

%files inets
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/inets-*/
%{_libdir}/erlang/lib/inets-*/ebin
%{_libdir}/erlang/lib/inets-*/priv
%{_libdir}/erlang/lib/inets-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/ftp.*
%{_libdir}/erlang/man/man3/httpc.*
%{_libdir}/erlang/man/man3/httpd.*
%{_libdir}/erlang/man/man3/httpd_conf.*
%{_libdir}/erlang/man/man3/httpd_socket.*
%{_libdir}/erlang/man/man3/httpd_util.*
%{_libdir}/erlang/man/man3/inets.*
%{_libdir}/erlang/man/man3/mod_alias.*
%{_libdir}/erlang/man/man3/mod_auth.*
%{_libdir}/erlang/man/man3/mod_esi.*
%{_libdir}/erlang/man/man3/mod_security.*
%{_libdir}/erlang/man/man3/tftp.*
%endif

%files inviso
%defattr(-,root,root)
%{_libdir}/erlang/lib/inviso-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/inviso.*
%{_libdir}/erlang/man/man3/inviso_as_lib.*
%{_libdir}/erlang/man/man3/inviso_lfm.*
%{_libdir}/erlang/man/man3/inviso_lfm_tpfreader.*
%{_libdir}/erlang/man/man3/inviso_rt.*
%{_libdir}/erlang/man/man3/inviso_rt_meta.*
%endif

%files jinterface
%defattr(-,root,root)
%{_libdir}/erlang/lib/jinterface-*/

%files kernel
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/kernel-*/
%{_libdir}/erlang/lib/kernel-*/ebin
%{_libdir}/erlang/lib/kernel-*/include
%{_libdir}/erlang/lib/kernel-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/application.*
%{_libdir}/erlang/man/man3/auth.*
%{_libdir}/erlang/man/man3/code.*
%{_libdir}/erlang/man/man3/disk_log.*
%{_libdir}/erlang/man/man3/erl_boot_server.*
%{_libdir}/erlang/man/man3/erl_ddll.*
%{_libdir}/erlang/man/man3/erl_prim_loader_stub.*
%{_libdir}/erlang/man/man3/erlang_stub.*
%{_libdir}/erlang/man/man3/error_handler.*
%{_libdir}/erlang/man/man3/error_logger.*
%{_libdir}/erlang/man/man3/file.*
%{_libdir}/erlang/man/man3/gen_sctp.*
%{_libdir}/erlang/man/man3/gen_tcp.*
%{_libdir}/erlang/man/man3/gen_udp.*
%{_libdir}/erlang/man/man3/global.*
%{_libdir}/erlang/man/man3/global_group.*
%{_libdir}/erlang/man/man3/heart.*
%{_libdir}/erlang/man/man3/inet.*
%{_libdir}/erlang/man/man3/inet_res.*
%{_libdir}/erlang/man/man3/init_stub.*
%{_libdir}/erlang/man/man3/net_adm.*
%{_libdir}/erlang/man/man3/net_kernel.*
%{_libdir}/erlang/man/man3/os.*
%{_libdir}/erlang/man/man3/packages.*
%{_libdir}/erlang/man/man3/pg2.*
%{_libdir}/erlang/man/man3/rpc.*
%{_libdir}/erlang/man/man3/seq_trace.*
%{_libdir}/erlang/man/man3/user.*
%{_libdir}/erlang/man/man3/wrap_log_reader.*
%{_libdir}/erlang/man/man3/zlib_stub.*
%{_libdir}/erlang/man/man4/app.*
%{_libdir}/erlang/man/man4/config.*
%{_libdir}/erlang/man/man6/kernel.*
%endif

%files megaco
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/megaco-*/
%{_libdir}/erlang/lib/megaco-*/ebin
%{_libdir}/erlang/lib/megaco-*/include
%{_libdir}/erlang/lib/megaco-*/priv
%{_libdir}/erlang/lib/megaco-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/megaco.*
%{_libdir}/erlang/man/man3/megaco_codec_meas.*
%{_libdir}/erlang/man/man3/megaco_codec_mstone1.*
%{_libdir}/erlang/man/man3/megaco_codec_mstone2.*
%{_libdir}/erlang/man/man3/megaco_codec_transform.*
%{_libdir}/erlang/man/man3/megaco_edist_compress.*
%{_libdir}/erlang/man/man3/megaco_encoder.*
%{_libdir}/erlang/man/man3/megaco_flex_scanner.*
%{_libdir}/erlang/man/man3/megaco_tcp.*
%{_libdir}/erlang/man/man3/megaco_transport.*
%{_libdir}/erlang/man/man3/megaco_udp.*
%{_libdir}/erlang/man/man3/megaco_user.*
%endif

%files mnesia
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/mnesia-*/
%{_libdir}/erlang/lib/mnesia-*/ebin
%{_libdir}/erlang/lib/mnesia-*/include
%{_libdir}/erlang/lib/mnesia-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/mnesia.*
%{_libdir}/erlang/man/man3/mnesia_frag_hash.*
%{_libdir}/erlang/man/man3/mnesia_registry.*
%endif

%files observer
%defattr(-,root,root)
%{_libdir}/erlang/lib/observer-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/crashdump.*
%{_libdir}/erlang/man/man3/ttb.*
%{_libdir}/erlang/man/man6/observer.*
%endif

%files odbc
%defattr(-,root,root)
%{_libdir}/erlang/lib/odbc-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/odbc.*
%endif

%files orber
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/orber-*/
%{_libdir}/erlang/lib/orber-*/COSS
%{_libdir}/erlang/lib/orber-*/ebin
%{_libdir}/erlang/lib/orber-*/include
%{_libdir}/erlang/lib/orber-*/java_src
%{_libdir}/erlang/lib/orber-*/priv
%{_libdir}/erlang/lib/orber-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/CosNaming.*
%{_libdir}/erlang/man/man3/CosNaming_BindingIterator.*
%{_libdir}/erlang/man/man3/CosNaming_NamingContext.*
%{_libdir}/erlang/man/man3/CosNaming_NamingContextExt.*
%{_libdir}/erlang/man/man3/Module_Interface.*
%{_libdir}/erlang/man/man3/any.*
%{_libdir}/erlang/man/man3/corba.*
%{_libdir}/erlang/man/man3/corba_object.*
%{_libdir}/erlang/man/man3/etop.*
%{_libdir}/erlang/man/man3/fixed.*
%{_libdir}/erlang/man/man3/interceptors.*
%{_libdir}/erlang/man/man3/lname.*
%{_libdir}/erlang/man/man3/lname_component.*
%{_libdir}/erlang/man/man3/orber.*
%{_libdir}/erlang/man/man3/orber_acl.*
%{_libdir}/erlang/man/man3/orber_diagnostics.*
%{_libdir}/erlang/man/man3/orber_ifr.*
%{_libdir}/erlang/man/man3/orber_tc.*
%endif

%files os_mon
%defattr(-,root,root)
%{_libdir}/erlang/lib/os_mon-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/cpu_sup.*
%{_libdir}/erlang/man/man3/disksup.*
%{_libdir}/erlang/man/man3/memsup.*
%{_libdir}/erlang/man/man3/os_mon_mib.*
%{_libdir}/erlang/man/man3/os_sup.*
%{_libdir}/erlang/man/man6/os_mon.*
%endif

%files otp_mibs
%defattr(-,root,root)
%{_libdir}/erlang/lib/otp_mibs-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/otp_mib.*
%endif

%files parsetools
%defattr(-,root,root)
%{_libdir}/erlang/lib/parsetools-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/leex.*
%{_libdir}/erlang/man/man3/yecc.*
%endif

%files percept
%defattr(-,root,root)
%{_libdir}/erlang/lib/percept-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/egd.*
%{_libdir}/erlang/man/man3/percept.*
%{_libdir}/erlang/man/man3/percept_profile.*
%endif

%files pman
%defattr(-,root,root)
%{_libdir}/erlang/lib/pman-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/pman.*
%endif

%files public_key
%defattr(-,root,root)
%{_libdir}/erlang/lib/public_key-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/public_key.*
%endif

%files reltool
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/reltool-*/
%{_libdir}/erlang/lib/reltool-*/ebin
%{_libdir}/erlang/lib/reltool-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/reltool.*
%endif

%files rpm-macros
%defattr(-,root,root)
%{_sysconfdir}/rpm/macros.erlang
%{_rpmconfigdir}/erlang-find-provides.escript
%{_rpmconfigdir}/erlang-find-provides.sh
%{_rpmconfigdir}/erlang-find-requires.escript
%{_rpmconfigdir}/erlang-find-requires.sh

%files runtime_tools
%defattr(-,root,root)
%{_libdir}/erlang/lib/runtime_tools-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/dbg.*
%{_libdir}/erlang/man/man3/erts_alloc_config.*
%{_libdir}/erlang/man/man6/runtime_tools.*
%endif

%files sasl
%defattr(-,root,root)
%{_libdir}/erlang/lib/sasl-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/alarm_handler.*
%{_libdir}/erlang/man/man3/overload.*
%{_libdir}/erlang/man/man3/rb.*
%{_libdir}/erlang/man/man3/release_handler.*
%{_libdir}/erlang/man/man3/systools.*
%{_libdir}/erlang/man/man4/appup.*
%{_libdir}/erlang/man/man4/rel.*
%{_libdir}/erlang/man/man4/relup.*
%{_libdir}/erlang/man/man4/script.*
%{_libdir}/erlang/man/man6/sasl.*
%endif

%files snmp
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/snmp-*/
%{_libdir}/erlang/lib/snmp-*/ebin
%{_libdir}/erlang/lib/snmp-*/include
%{_libdir}/erlang/lib/snmp-*/mibs
%{_libdir}/erlang/lib/snmp-*/priv
%{_libdir}/erlang/lib/snmp-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/snmp.*
%{_libdir}/erlang/man/man3/snmpa.*
%{_libdir}/erlang/man/man3/snmpa_conf.*
%{_libdir}/erlang/man/man3/snmpa_discovery_handler.*
%{_libdir}/erlang/man/man3/snmpa_error.*
%{_libdir}/erlang/man/man3/snmpa_error_io.*
%{_libdir}/erlang/man/man3/snmpa_error_logger.*
%{_libdir}/erlang/man/man3/snmpa_error_report.*
%{_libdir}/erlang/man/man3/snmpa_local_db.*
%{_libdir}/erlang/man/man3/snmpa_mpd.*
%{_libdir}/erlang/man/man3/snmpa_network_interface.*
%{_libdir}/erlang/man/man3/snmpa_network_interface_filter.*
%{_libdir}/erlang/man/man3/snmpa_notification_delivery_info_receiver.*
%{_libdir}/erlang/man/man3/snmpa_notification_filter.*
%{_libdir}/erlang/man/man3/snmpa_supervisor.*
%{_libdir}/erlang/man/man3/snmpc.*
%{_libdir}/erlang/man/man3/snmp_community_mib.*
%{_libdir}/erlang/man/man3/snmp_framework_mib.*
%{_libdir}/erlang/man/man3/snmp_generic.*
%{_libdir}/erlang/man/man3/snmp_index.*
%{_libdir}/erlang/man/man3/snmpm.*
%{_libdir}/erlang/man/man3/snmpm_conf.*
%{_libdir}/erlang/man/man3/snmpm_mpd.*
%{_libdir}/erlang/man/man3/snmpm_network_interface.*
%{_libdir}/erlang/man/man3/snmpm_network_interface_filter.*
%{_libdir}/erlang/man/man3/snmpm_user.*
%{_libdir}/erlang/man/man3/snmp_notification_mib.*
%{_libdir}/erlang/man/man3/snmp_pdus.*
%{_libdir}/erlang/man/man3/snmp_standard_mib.*
%{_libdir}/erlang/man/man3/snmp_target_mib.*
%{_libdir}/erlang/man/man3/snmp_user_based_sm_mib.*
%{_libdir}/erlang/man/man3/snmp_view_based_acm_mib.*
%{_libdir}/erlang/man/man6/snmp.*
%{_libdir}/erlang/man/man7/INET-ADDRESS-MIB.*
%{_libdir}/erlang/man/man7/OTP-SNMPEA-MIB.*
%{_libdir}/erlang/man/man7/RFC1213-MIB.*
%{_libdir}/erlang/man/man7/SNMP-COMMUNITY-MIB.*
%{_libdir}/erlang/man/man7/SNMP-FRAMEWORK-MIB.*
%{_libdir}/erlang/man/man7/SNMP-MPD-MIB.*
%{_libdir}/erlang/man/man7/SNMP-NOTIFICATION-MIB.*
%{_libdir}/erlang/man/man7/SNMP-TARGET-MIB.*
%{_libdir}/erlang/man/man7/SNMP-USER-BASED-SM-MIB.*
%{_libdir}/erlang/man/man7/SNMP-USM-AES-MIB.*
%{_libdir}/erlang/man/man7/SNMPv2-MIB.*
%{_libdir}/erlang/man/man7/SNMPv2-TM.*
%{_libdir}/erlang/man/man7/SNMP-VIEW-BASED-ACM-MIB.*
%{_libdir}/erlang/man/man7/STANDARD-MIB.*
%endif

%files ssh
%defattr(-,root,root)
%{_libdir}/erlang/lib/ssh-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/ssh.*
%{_libdir}/erlang/man/man3/ssh_channel.*
%{_libdir}/erlang/man/man3/ssh_connection.*
%{_libdir}/erlang/man/man3/ssh_sftp.*
%{_libdir}/erlang/man/man3/ssh_sftpd.*
%endif

%files ssl
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/ssl-*/
%{_libdir}/erlang/lib/ssl-*/ebin
%{_libdir}/erlang/lib/ssl-*/priv
%{_libdir}/erlang/lib/ssl-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/old_ssl.*
%{_libdir}/erlang/man/man3/ssl.*
%{_libdir}/erlang/man/man3/ssl_session_cache_api.*
%{_libdir}/erlang/man/man6/ssl.*
%endif

%files stdlib
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/stdlib-*/
%{_libdir}/erlang/lib/stdlib-*/ebin
%{_libdir}/erlang/lib/stdlib-*/include
%{_libdir}/erlang/lib/stdlib-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/array.*
%{_libdir}/erlang/man/man3/base64.*
%{_libdir}/erlang/man/man3/beam_lib.*
%{_libdir}/erlang/man/man3/binary.*
%{_libdir}/erlang/man/man3/c.*
%{_libdir}/erlang/man/man3/calendar.*
%{_libdir}/erlang/man/man3/dets.*
%{_libdir}/erlang/man/man3/dict.*
%{_libdir}/erlang/man/man3/digraph.*
%{_libdir}/erlang/man/man3/digraph_utils.*
%{_libdir}/erlang/man/man3/epp.*
%{_libdir}/erlang/man/man3/erl_eval.*
%{_libdir}/erlang/man/man3/erl_expand_records.*
%{_libdir}/erlang/man/man3/erl_id_trans.*
%{_libdir}/erlang/man/man3/erl_internal.*
%{_libdir}/erlang/man/man3/erl_lint.*
%{_libdir}/erlang/man/man3/erl_parse.*
%{_libdir}/erlang/man/man3/erl_pp.*
%{_libdir}/erlang/man/man3/erl_scan.*
%{_libdir}/erlang/man/man3/erl_tar.*
%{_libdir}/erlang/man/man3/ets.*
%{_libdir}/erlang/man/man3/file_sorter.*
%{_libdir}/erlang/man/man3/filelib.*
%{_libdir}/erlang/man/man3/filename.*
%{_libdir}/erlang/man/man3/gb_sets.*
%{_libdir}/erlang/man/man3/gb_trees.*
%{_libdir}/erlang/man/man3/gen_event.*
%{_libdir}/erlang/man/man3/gen_fsm.*
%{_libdir}/erlang/man/man3/gen_server.*
%{_libdir}/erlang/man/man3/io.*
%{_libdir}/erlang/man/man3/io_lib.*
%{_libdir}/erlang/man/man3/lib.*
%{_libdir}/erlang/man/man3/lists.*
%{_libdir}/erlang/man/man3/log_mf_h.*
%{_libdir}/erlang/man/man3/math.*
%{_libdir}/erlang/man/man3/ms_transform.*
%{_libdir}/erlang/man/man3/orddict.*
%{_libdir}/erlang/man/man3/ordsets.*
%{_libdir}/erlang/man/man3/pg.*
%{_libdir}/erlang/man/man3/pool.*
%{_libdir}/erlang/man/man3/proc_lib.*
%{_libdir}/erlang/man/man3/proplists.*
%{_libdir}/erlang/man/man3/qlc.*
%{_libdir}/erlang/man/man3/queue.*
%{_libdir}/erlang/man/man3/random.*
%{_libdir}/erlang/man/man3/re.*
%{_libdir}/erlang/man/man3/regexp.*
%{_libdir}/erlang/man/man3/sets.*
%{_libdir}/erlang/man/man3/shell.*
%{_libdir}/erlang/man/man3/shell_default.*
%{_libdir}/erlang/man/man3/slave.*
%{_libdir}/erlang/man/man3/sofs.*
%{_libdir}/erlang/man/man3/string.*
%{_libdir}/erlang/man/man3/supervisor.*
%{_libdir}/erlang/man/man3/supervisor_bridge.*
%{_libdir}/erlang/man/man3/sys.*
%{_libdir}/erlang/man/man3/timer.*
%{_libdir}/erlang/man/man3/unicode.*
%{_libdir}/erlang/man/man3/zip.*
%{_libdir}/erlang/man/man6/stdlib.*
%endif

%files syntax_tools
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/syntax_tools-*/
%{_libdir}/erlang/lib/syntax_tools-*/ebin
%if %{with doc}
%{_libdir}/erlang/man/man3/epp_dodger.*
%{_libdir}/erlang/man/man3/erl_comment_scan.*
%{_libdir}/erlang/man/man3/erl_prettypr.*
%{_libdir}/erlang/man/man3/erl_recomment.*
%{_libdir}/erlang/man/man3/erl_syntax.*
%{_libdir}/erlang/man/man3/erl_syntax_lib.*
%{_libdir}/erlang/man/man3/erl_tidy.*
%{_libdir}/erlang/man/man3/igor.*
%{_libdir}/erlang/man/man3/prettypr.*
%endif

%files test_server
%defattr(-,root,root)
%{_libdir}/erlang/lib/test_server-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/test_server.*
%{_libdir}/erlang/man/man3/test_server_ctrl.*
%{_libdir}/erlang/man/man6/test_server.*
%endif

%files toolbar
%defattr(-,root,root)
%{_libdir}/erlang/lib/toolbar-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/toolbar.*
%endif

%files tools
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/tools-*/
%{_libdir}/erlang/lib/tools-*/bin
%{_libdir}/erlang/lib/tools-*/ebin
%{_libdir}/erlang/lib/tools-*/emacs
%{_libdir}/erlang/lib/tools-*/priv
%{_libdir}/erlang/lib/tools-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/cover.*
%{_libdir}/erlang/man/man3/cprof.*
%{_libdir}/erlang/man/man3/eprof.*
%{_libdir}/erlang/man/man3/erlang_mode.*
%{_libdir}/erlang/man/man3/fprof.*
%{_libdir}/erlang/man/man3/instrument.*
%{_libdir}/erlang/man/man3/lcnt.*
%{_libdir}/erlang/man/man3/make.*
%{_libdir}/erlang/man/man3/tags.*
%{_libdir}/erlang/man/man3/xref.*
%endif

%files tv
%defattr(-,root,root)
%{_libdir}/erlang/lib/tv-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/tv.*
%endif

%files typer
%defattr(-,root,root)
%{_bindir}/typer
%{_libdir}/erlang/bin/typer
%{_libdir}/erlang/erts-*/bin/typer
%{_libdir}/erlang/lib/typer-*/

%files webtool
%defattr(-,root,root)
%{_libdir}/erlang/lib/webtool-*/
%if %{with doc}
%{_libdir}/erlang/man/man1/start_webtool.*
%{_libdir}/erlang/man/man3/webtool.*
%endif

%files wx
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/wx-*/
%{_libdir}/erlang/lib/wx-*/ebin
%{_libdir}/erlang/lib/wx-*/include
%{_libdir}/erlang/lib/wx-*/priv
%{_libdir}/erlang/lib/wx-*/src
%if %{with doc}
%{_libdir}/erlang/man/man3/gl.*
%{_libdir}/erlang/man/man3/glu.*
%{_libdir}/erlang/man/man3/wx.*
%{_libdir}/erlang/man/man3/wx_misc.*
%{_libdir}/erlang/man/man3/wx_object.*
%{_libdir}/erlang/man/man3/wxAcceleratorEntry.*
%{_libdir}/erlang/man/man3/wxAcceleratorTable.*
%{_libdir}/erlang/man/man3/wxArtProvider.*
%{_libdir}/erlang/man/man3/wxAuiDockArt.*
%{_libdir}/erlang/man/man3/wxAuiManager.*
%{_libdir}/erlang/man/man3/wxAuiManagerEvent.*
%{_libdir}/erlang/man/man3/wxAuiNotebook.*
%{_libdir}/erlang/man/man3/wxAuiNotebookEvent.*
%{_libdir}/erlang/man/man3/wxAuiPaneInfo.*
%{_libdir}/erlang/man/man3/wxAuiTabArt.*
%{_libdir}/erlang/man/man3/wxBitmap.*
%{_libdir}/erlang/man/man3/wxBitmapButton.*
%{_libdir}/erlang/man/man3/wxBitmapDataObject.*
%{_libdir}/erlang/man/man3/wxBoxSizer.*
%{_libdir}/erlang/man/man3/wxBrush.*
%{_libdir}/erlang/man/man3/wxBufferedDC.*
%{_libdir}/erlang/man/man3/wxBufferedPaintDC.*
%{_libdir}/erlang/man/man3/wxButton.*
%{_libdir}/erlang/man/man3/wxCalendarCtrl.*
%{_libdir}/erlang/man/man3/wxCalendarDateAttr.*
%{_libdir}/erlang/man/man3/wxCalendarEvent.*
%{_libdir}/erlang/man/man3/wxCaret.*
%{_libdir}/erlang/man/man3/wxCheckBox.*
%{_libdir}/erlang/man/man3/wxCheckListBox.*
%{_libdir}/erlang/man/man3/wxChildFocusEvent.*
%{_libdir}/erlang/man/man3/wxChoice.*
%{_libdir}/erlang/man/man3/wxChoicebook.*
%{_libdir}/erlang/man/man3/wxClientDC.*
%{_libdir}/erlang/man/man3/wxClipboard.*
%{_libdir}/erlang/man/man3/wxCloseEvent.*
%{_libdir}/erlang/man/man3/wxColourData.*
%{_libdir}/erlang/man/man3/wxColourDialog.*
%{_libdir}/erlang/man/man3/wxColourPickerCtrl.*
%{_libdir}/erlang/man/man3/wxColourPickerEvent.*
%{_libdir}/erlang/man/man3/wxComboBox.*
%{_libdir}/erlang/man/man3/wxCommandEvent.*
%{_libdir}/erlang/man/man3/wxContextMenuEvent.*
%{_libdir}/erlang/man/man3/wxControl.*
%{_libdir}/erlang/man/man3/wxControlWithItems.*
%{_libdir}/erlang/man/man3/wxCursor.*
%{_libdir}/erlang/man/man3/wxDataObject.*
%{_libdir}/erlang/man/man3/wxDateEvent.*
%{_libdir}/erlang/man/man3/wxDatePickerCtrl.*
%{_libdir}/erlang/man/man3/wxDC.*
%{_libdir}/erlang/man/man3/wxDialog.*
%{_libdir}/erlang/man/man3/wxDirDialog.*
%{_libdir}/erlang/man/man3/wxDirPickerCtrl.*
%{_libdir}/erlang/man/man3/wxDisplayChangedEvent.*
%{_libdir}/erlang/man/man3/wxEraseEvent.*
%{_libdir}/erlang/man/man3/wxEvent.*
%{_libdir}/erlang/man/man3/wxEvtHandler.*
%{_libdir}/erlang/man/man3/wxFileDataObject.*
%{_libdir}/erlang/man/man3/wxFileDialog.*
%{_libdir}/erlang/man/man3/wxFileDirPickerEvent.*
%{_libdir}/erlang/man/man3/wxFilePickerCtrl.*
%{_libdir}/erlang/man/man3/wxFindReplaceData.*
%{_libdir}/erlang/man/man3/wxFindReplaceDialog.*
%{_libdir}/erlang/man/man3/wxFlexGridSizer.*
%{_libdir}/erlang/man/man3/wxFocusEvent.*
%{_libdir}/erlang/man/man3/wxFont.*
%{_libdir}/erlang/man/man3/wxFontData.*
%{_libdir}/erlang/man/man3/wxFontDialog.*
%{_libdir}/erlang/man/man3/wxFontPickerCtrl.*
%{_libdir}/erlang/man/man3/wxFontPickerEvent.*
%{_libdir}/erlang/man/man3/wxFrame.*
%{_libdir}/erlang/man/man3/wxGauge.*
%{_libdir}/erlang/man/man3/wxGBSizerItem.*
%{_libdir}/erlang/man/man3/wxGenericDirCtrl.*
%{_libdir}/erlang/man/man3/wxGLCanvas.*
%{_libdir}/erlang/man/man3/wxGraphicsBrush.*
%{_libdir}/erlang/man/man3/wxGraphicsContext.*
%{_libdir}/erlang/man/man3/wxGraphicsFont.*
%{_libdir}/erlang/man/man3/wxGraphicsMatrix.*
%{_libdir}/erlang/man/man3/wxGraphicsObject.*
%{_libdir}/erlang/man/man3/wxGraphicsPath.*
%{_libdir}/erlang/man/man3/wxGraphicsPen.*
%{_libdir}/erlang/man/man3/wxGraphicsRenderer.*
%{_libdir}/erlang/man/man3/wxGrid.*
%{_libdir}/erlang/man/man3/wxGridBagSizer.*
%{_libdir}/erlang/man/man3/wxGridCellAttr.*
%{_libdir}/erlang/man/man3/wxGridCellBoolEditor.*
%{_libdir}/erlang/man/man3/wxGridCellBoolRenderer.*
%{_libdir}/erlang/man/man3/wxGridCellChoiceEditor.*
%{_libdir}/erlang/man/man3/wxGridCellEditor.*
%{_libdir}/erlang/man/man3/wxGridCellFloatEditor.*
%{_libdir}/erlang/man/man3/wxGridCellFloatRenderer.*
%{_libdir}/erlang/man/man3/wxGridCellNumberEditor.*
%{_libdir}/erlang/man/man3/wxGridCellNumberRenderer.*
%{_libdir}/erlang/man/man3/wxGridCellRenderer.*
%{_libdir}/erlang/man/man3/wxGridCellStringRenderer.*
%{_libdir}/erlang/man/man3/wxGridCellTextEditor.*
%{_libdir}/erlang/man/man3/wxGridEvent.*
%{_libdir}/erlang/man/man3/wxGridSizer.*
%{_libdir}/erlang/man/man3/wxHelpEvent.*
%{_libdir}/erlang/man/man3/wxHtmlEasyPrinting.*
%{_libdir}/erlang/man/man3/wxHtmlLinkEvent.*
%{_libdir}/erlang/man/man3/wxHtmlWindow.*
%{_libdir}/erlang/man/man3/wxIcon.*
%{_libdir}/erlang/man/man3/wxIconBundle.*
%{_libdir}/erlang/man/man3/wxIconizeEvent.*
%{_libdir}/erlang/man/man3/wxIdleEvent.*
%{_libdir}/erlang/man/man3/wxImage.*
%{_libdir}/erlang/man/man3/wxImageList.*
%{_libdir}/erlang/man/man3/wxJoystickEvent.*
%{_libdir}/erlang/man/man3/wxKeyEvent.*
%{_libdir}/erlang/man/man3/wxLayoutAlgorithm.*
%{_libdir}/erlang/man/man3/wxListbook.*
%{_libdir}/erlang/man/man3/wxListBox.*
%{_libdir}/erlang/man/man3/wxListCtrl.*
%{_libdir}/erlang/man/man3/wxListEvent.*
%{_libdir}/erlang/man/man3/wxListItem.*
%{_libdir}/erlang/man/man3/wxListView.*
%{_libdir}/erlang/man/man3/wxLogNull.*
%{_libdir}/erlang/man/man3/wxMask.*
%{_libdir}/erlang/man/man3/wxMaximizeEvent.*
%{_libdir}/erlang/man/man3/wxMDIChildFrame.*
%{_libdir}/erlang/man/man3/wxMDIClientWindow.*
%{_libdir}/erlang/man/man3/wxMDIParentFrame.*
%{_libdir}/erlang/man/man3/wxMemoryDC.*
%{_libdir}/erlang/man/man3/wxMenu.*
%{_libdir}/erlang/man/man3/wxMenuBar.*
%{_libdir}/erlang/man/man3/wxMenuEvent.*
%{_libdir}/erlang/man/man3/wxMenuItem.*
%{_libdir}/erlang/man/man3/wxMessageDialog.*
%{_libdir}/erlang/man/man3/wxMiniFrame.*
%{_libdir}/erlang/man/man3/wxMirrorDC.*
%{_libdir}/erlang/man/man3/wxMouseCaptureChangedEvent.*
%{_libdir}/erlang/man/man3/wxMouseEvent.*
%{_libdir}/erlang/man/man3/wxMoveEvent.*
%{_libdir}/erlang/man/man3/wxMultiChoiceDialog.*
%{_libdir}/erlang/man/man3/wxNavigationKeyEvent.*
%{_libdir}/erlang/man/man3/wxNcPaintEvent.*
%{_libdir}/erlang/man/man3/wxNotebook.*
%{_libdir}/erlang/man/man3/wxNotebookEvent.*
%{_libdir}/erlang/man/man3/wxNotifyEvent.*
%{_libdir}/erlang/man/man3/wxPageSetupDialog.*
%{_libdir}/erlang/man/man3/wxPageSetupDialogData.*
%{_libdir}/erlang/man/man3/wxPaintDC.*
%{_libdir}/erlang/man/man3/wxPaintEvent.*
%{_libdir}/erlang/man/man3/wxPalette.*
%{_libdir}/erlang/man/man3/wxPaletteChangedEvent.*
%{_libdir}/erlang/man/man3/wxPanel.*
%{_libdir}/erlang/man/man3/wxPasswordEntryDialog.*
%{_libdir}/erlang/man/man3/wxPen.*
%{_libdir}/erlang/man/man3/wxPickerBase.*
%{_libdir}/erlang/man/man3/wxPostScriptDC.*
%{_libdir}/erlang/man/man3/wxPreviewCanvas.*
%{_libdir}/erlang/man/man3/wxPreviewControlBar.*
%{_libdir}/erlang/man/man3/wxPreviewFrame.*
%{_libdir}/erlang/man/man3/wxPrintData.*
%{_libdir}/erlang/man/man3/wxPrintDialog.*
%{_libdir}/erlang/man/man3/wxPrintDialogData.*
%{_libdir}/erlang/man/man3/wxPrinter.*
%{_libdir}/erlang/man/man3/wxPrintout.*
%{_libdir}/erlang/man/man3/wxPrintPreview.*
%{_libdir}/erlang/man/man3/wxProgressDialog.*
%{_libdir}/erlang/man/man3/wxQueryNewPaletteEvent.*
%{_libdir}/erlang/man/man3/wxRadioBox.*
%{_libdir}/erlang/man/man3/wxRadioButton.*
%{_libdir}/erlang/man/man3/wxRegion.*
%{_libdir}/erlang/man/man3/wxSashEvent.*
%{_libdir}/erlang/man/man3/wxSashLayoutWindow.*
%{_libdir}/erlang/man/man3/wxSashWindow.*
%{_libdir}/erlang/man/man3/wxScreenDC.*
%{_libdir}/erlang/man/man3/wxScrollBar.*
%{_libdir}/erlang/man/man3/wxScrolledWindow.*
%{_libdir}/erlang/man/man3/wxScrollEvent.*
%{_libdir}/erlang/man/man3/wxScrollWinEvent.*
%{_libdir}/erlang/man/man3/wxSetCursorEvent.*
%{_libdir}/erlang/man/man3/wxShowEvent.*
%{_libdir}/erlang/man/man3/wxSingleChoiceDialog.*
%{_libdir}/erlang/man/man3/wxSizeEvent.*
%{_libdir}/erlang/man/man3/wxSizer.*
%{_libdir}/erlang/man/man3/wxSizerFlags.*
%{_libdir}/erlang/man/man3/wxSizerItem.*
%{_libdir}/erlang/man/man3/wxSlider.*
%{_libdir}/erlang/man/man3/wxSpinButton.*
%{_libdir}/erlang/man/man3/wxSpinCtrl.*
%{_libdir}/erlang/man/man3/wxSpinEvent.*
%{_libdir}/erlang/man/man3/wxSplashScreen.*
%{_libdir}/erlang/man/man3/wxSplitterEvent.*
%{_libdir}/erlang/man/man3/wxSplitterWindow.*
%{_libdir}/erlang/man/man3/wxStaticBitmap.*
%{_libdir}/erlang/man/man3/wxStaticBox.*
%{_libdir}/erlang/man/man3/wxStaticBoxSizer.*
%{_libdir}/erlang/man/man3/wxStaticLine.*
%{_libdir}/erlang/man/man3/wxStaticText.*
%{_libdir}/erlang/man/man3/wxStatusBar.*
%{_libdir}/erlang/man/man3/wxStdDialogButtonSizer.*
%{_libdir}/erlang/man/man3/wxStyledTextCtrl.*
%{_libdir}/erlang/man/man3/wxStyledTextEvent.*
%{_libdir}/erlang/man/man3/wxSysColourChangedEvent.*
%{_libdir}/erlang/man/man3/wxTextAttr.*
%{_libdir}/erlang/man/man3/wxTextCtrl.*
%{_libdir}/erlang/man/man3/wxTextDataObject.*
%{_libdir}/erlang/man/man3/wxTextEntryDialog.*
%{_libdir}/erlang/man/man3/wxToggleButton.*
%{_libdir}/erlang/man/man3/wxToolBar.*
%{_libdir}/erlang/man/man3/wxToolbook.*
%{_libdir}/erlang/man/man3/wxToolTip.*
%{_libdir}/erlang/man/man3/wxTopLevelWindow.*
%{_libdir}/erlang/man/man3/wxTreebook.*
%{_libdir}/erlang/man/man3/wxTreeCtrl.*
%{_libdir}/erlang/man/man3/wxTreeEvent.*
%{_libdir}/erlang/man/man3/wxUpdateUIEvent.*
%{_libdir}/erlang/man/man3/wxWindow.*
%{_libdir}/erlang/man/man3/wxWindowCreateEvent.*
%{_libdir}/erlang/man/man3/wxWindowDC.*
%{_libdir}/erlang/man/man3/wxWindowDestroyEvent.*
%{_libdir}/erlang/man/man3/wxXmlResource.*
%endif

%files xmerl
%defattr(-,root,root)
%{_libdir}/erlang/lib/xmerl-*/
%if %{with doc}
%{_libdir}/erlang/man/man3/xmerl.*
%{_libdir}/erlang/man/man3/xmerl_eventp.*
%{_libdir}/erlang/man/man3/xmerl_sax_parser.*
%{_libdir}/erlang/man/man3/xmerl_scan.*
%{_libdir}/erlang/man/man3/xmerl_xpath.*
%{_libdir}/erlang/man/man3/xmerl_xs.*
%{_libdir}/erlang/man/man3/xmerl_xsd.*
%endif

%files -n emacs-erlang
%defattr(-,root,root,-)
%dir %{_emacs_sitelispdir}/erlang
%doc %{_emacs_sitelispdir}/erlang/README
%{_emacs_sitelispdir}/erlang/*.elc
%{_emacs_sitestartdir}/erlang-init.el

%files -n emacs-erlang-el
%defattr(-,root,root,-)
%{_emacs_sitelispdir}/erlang/*.el

%files -n xemacs-erlang
%defattr(-,root,root,-)
%dir %{_xemacs_sitelispdir}/erlang
%doc %{_xemacs_sitelispdir}/erlang/README
%{_xemacs_sitelispdir}/erlang/*.elc
%{_xemacs_sitestartdir}/erlang-init.el

%files -n xemacs-erlang-el
%defattr(-,root,root,-)
%{_xemacs_sitelispdir}/erlang/*.el


%changelog
* Wed Sep 29 2010 jkeating - R14B-0.1.1
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 Peter Lemenkov <lemenkov@gmail.com> - R14B-0.1
- R14B release

* Mon Aug  2 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14A-0.6
- Implement '--without doc' conditional for faster test builds (#618245).

* Fri Jul 30 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14A-0.5
- Properly hook up (X)Emacs erlang-mode (#491165)

* Mon Jul 26 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14A-0.4
- Spec file cleanups:
  - Avoid accidental %%rel increments by rpmdev-bumpspec.
  - Use %%global for our spec file macros.
  - Use macro for redundant directory names.
  - Whitespace cleanups (tabs vs. spaces).
  - Fix accidental macro usage in %%changelog.

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - R14A-0.3
- rebuilt against wxGTK-2.8.11-2

* Sat Jun 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R14A-0.2
- Updated list of explicit requirements

* Fri Jun 18 2010 Peter Lemenkov <lemenkov@gmail.com> - R14A-0.1
- R14A release

* Sat May 15 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.12
- Moved dialyzer and typer executables from erts to appropriate rpms

* Fri May 14 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.11
- Do not mention nteventlog in os_mon.app, see rhbz #592251

* Thu May  6 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.10
- Disabled automatic requires/provides generation

* Wed Apr 28 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.9
- Added missing files, necessary for emacs (see rhbz #585349)
- Patches rebased

* Tue Apr 27 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.8
- Added missing BuildRequires libxslt (for building docs)
- Removed %%post script completely (resolves rhbz #586428)
- Since now both docs and man-pages are built from sources
- No need to manually create symlinks in %%{_bindir}

* Mon Apr 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.7
- Build with erlang-rpm-macros
- Man-files are packed with packages, they belong to

* Mon Apr 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.6
- Made erlang-rpm-macros as separate package
- Fix error while installing erlang-rpm-macros

* Wed Apr 17 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.5
- Use erlang rpm macros for adding provides/reqires
- All %%{_libdir}/erlang/lib/* items were splitted off from main package, which
  in turn becomes purely virtual now.
- Removing RPM_BUILD_ROOT from several installed files is no longer required

* Sat Apr 17 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.4
- Added missing Requires mesa-libGL{U} for wx module (rhbz #583287)
- Fix for buffer overflow in pcre module (rhbz #583288)
- Doc sub-package marked as noarch (partially resolves rhbz #491165)

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
- link escript and dialyzer to %%{_bindir}

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
