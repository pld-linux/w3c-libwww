Summary:	HTTP library of common code
Name:		w3c-libwww
Version:	5.2.8
Release:	5
Copyright:	W3C (see: http://www.w3.org/Consortium/Legal/copyright-software.html)
Group:		Libraries
Source:		http://www.w3.org/Library/Distribution/%{name}-%{version}.tar.gz
Patch:		w3c-libwww-DESTDIR.patch
URL:		http://www.w3.org/Library
Icon:		Lib48x.gif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwww is a general-purpose Web API written in C for Unix and Windows
(Win32). With a highly extensible and layered API, it can accommodate many
different types of applications including clients, robots, etc. The purpose
of libwww is to provide a highly optimized HTTP sample implementation as
well as other Internet protocols and to serve as a testbed for protocol
experiments.

%package devel
Summary:	Libraries and header files for programs that use libwww
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for libwww, which are available as public libraries.

%package static
Summary:	Static libwww libraries
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libwww libraries.

%package apps
Summary:	Applications built using Libwww web library: e.g. Robot, command line tool, etc
Group:		Networking
Group(pl):	Aplikacje/Sieciowe
Requires:	%{name} = %{version}
Icon:		robot48x.gif

%description apps
Web applications built using Libwww: Robot, Command line tool, line mode
browser. The Robot can crawl web sites faster, and with lower load, than any
other web walker that we know of, due to its extensive pipelining and use of
HTTP/1.1. The command line tool (w3c) is very useful for manipulation of Web
sites that implement more than just HTTP GET (e.g. PUT, POST, etc.). The
line mode browser is a minimal line mode web browser; often useful to
convert to ascii text. Currently unavailable until someone updates it to
some new interfaces. (hint, hint...)

%prep
%setup -q
%patch -p1

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-shared \
	--with-gnu-ld \
	--with-regex \
	--with-zlib
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*
%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.html */*.html */*/*.html Icons/*/*.gif
%attr(755,root,root) %{_libdir}/libwww*.so.*.*
%attr(755,root,root) %{_libdir}/libxml*.so.*.*
%attr(755,root,root) %{_libdir}/libmd5.so.*.*
%{_datadir}/w3c-libwww

%files apps
%attr(755,root,root) %{_bindir}/webbot
%attr(755,root,root) %{_bindir}/w3c

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libwww-config
%attr(755,root,root) %{_libdir}/libwww*.so
%attr(755,root,root) %{_libdir}/libxml*.so
%attr(755,root,root) %{_libdir}/libmd5.so
%attr(755,root,root) %{_libdir}/libwww*.la
%attr(755,root,root) %{_libdir}/libxml*.la
%attr(755,root,root) %{_libdir}/libmd5.la

%{_includedir}/xmlparse.h
%{_includedir}/w3c-libwww

%files static
%defattr(644,root,root,755)
%{_libdir}/libwww*.a
%{_libdir}/libxml*.a
%{_libdir}/libmd5.a
