Summary:	HTTP library of common code
Summary(pl):	Biblioteka wspólnego kodu HTTP
Name:		w3c-libwww
Version:	5.3.2
Release:	1
License:	W3C (see: http://www.w3.org/Consortium/Legal/copyright-software.html)
Group:		Libraries
Source0:	http://www.w3.org/Library/Distribution/%{name}-%{version}.tar.gz
URL:		http://www.w3.org/Library/
Icon:		Lib48x.gif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwww is a general-purpose Web API written in C for Unix and Windows
(Win32). With a highly extensible and layered API, it can accommodate
many different types of applications including clients, robots, etc.
The purpose of libwww is to provide a highly optimized HTTP sample
implementation as well as other Internet protocols and to serve as a
testbed for protocol experiments.

%description -l pl
Libwww jest bibliotek± WWW ogólnego przeznaczenia napisan± w C dla
Uniksów oraz Windows. Z wysoko rozszerzalnym i warstwowym API, mo¿e
mieæ zastosowanie w wielu rodzajach aplikacji, w tym klientach,
robotach itp. Celem libwww jest dostarczenie dobrze zoptymalizowanej,
przyk³adowej implementacji HTTP, a tak¿e innych protoko³ów
internetowych, oraz ¶rodowiska testowego do eksperymentów z
protoko³ami.

%package devel
Summary:	Header files for programs that use libwww
Summary(pl):	Pliki nag³ówkowe dla programów u¿ywaj±cych libwww
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libwww, which are available as public libraries.

%description devel -l pl
Pliki nag³ówkowe dla libwww.

%package static
Summary:	Static libwww libraries
Summary(pl):	Statyczne biblioteki libwww
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libwww libraries.

%description static -l pl
Statyczne biblioteki libwww.

%package apps
Summary:	Applications built using Libwww web library: e.g. Robot, command line tool, etc
Summary(pl):	Aplikacje u¿ywaj±ce Libwww: Robot, narzêdzie command-line itp.
Group:		Applications/Networking
Requires:	%{name} = %{version}
Icon:		robot48x.gif

%description apps
Web applications built using Libwww: Robot, Command line tool, line
mode browser. The Robot can crawl web sites faster, and with lower
load, than any other web walker that we know of, due to its extensive
pipelining and use of HTTP/1.1. The command line tool (w3c) is very
useful for manipulation of Web sites that implement more than just
HTTP GET (e.g. PUT, POST, etc.). The line mode browser is a minimal
line mode web browser; often useful to convert to ascii text.
Currently unavailable until someone updates it to some new interfaces.
(hint, hint...)

%description apps -l pl
Aplikacje sieciowe zbudowane przy u¿yciu libwww: Robot, narzêdzie
comman-line, liniowa przegl±darka. Robot mo¿e przechodziæ po stronach
szybciej i z mniejszym obci±¿eniem ni¿ inne znane roboty, dziêki
wykorzystywaniu pipeliningu i HTTP/1.1. Narzêdzie command-line (w3c)
jest u¿yteczne do manipulowania serwisami WWW, które maj±
zaimplementowane co¶ wiêcej ni¿ HTTP GET (np. PUT, POST...).
Przegl±darka liniowa jest u¿yteczna g³ównie do konwersji do zwyk³ego
tekstu. Aktualnie niedostêpna dopóki kto¶ nie przystosuje jej do
nowego interfejsu (hint, hint...).

%prep
%setup -q

%build
%configure2_13 \
	--enable-shared \
	--with-gnu-ld \
	--with-regex \
	--with-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/libpics.so.*.*
%{_datadir}/w3c-libwww

%files apps
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/webbot
%attr(755,root,root) %{_bindir}/w3c
%attr(755,root,root) %{_bindir}/www

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libwww-config
%attr(755,root,root) %{_libdir}/libwww*.so
%attr(755,root,root) %{_libdir}/libxml*.so
%attr(755,root,root) %{_libdir}/libmd5.so
%attr(755,root,root) %{_libdir}/libpics.so
%attr(755,root,root) %{_libdir}/libwww*.la
%attr(755,root,root) %{_libdir}/libxml*.la
%attr(755,root,root) %{_libdir}/libmd5.la
%attr(755,root,root) %{_libdir}/libpics.la

%{_includedir}/wwwconf.h
%{_includedir}/w3c-libwww

%files static
%defattr(644,root,root,755)
%{_libdir}/libwww*.a
%{_libdir}/libxml*.a
%{_libdir}/libmd5.a
%{_libdir}/libpics.a
