Summary:	HTTP library of common code
Summary(pl):	Biblioteka wspÛlnego kodu HTTP
Name:		w3c-libwww
Version:	5.3.1
Release:	1
License:	W3C (see: http://www.w3.org/Consortium/Legal/copyright-software.html)
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://www.w3.org/Library/Distribution/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.w3.org/Library
Icon:		Lib48x.gif
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwww is a general-purpose Web API written in C for Unix and Windows
(Win32). With a highly extensible and layered API, it can accommodate
many different types of applications including clients, robots, etc.
The purpose of libwww is to provide a highly optimized HTTP sample
implementation as well as other Internet protocols and to serve as a
testbed for protocol experiments.

%description -l pl
Libwww jest bibliotek± WWW ogÛlnego przeznaczenia napisan± w C dla
UniksÛw oraz Windows. Z wysoko rozszerzalnym i warstwowym API, moøe
mieÊ zastosowanie w wielu rodzajach aplikacji, w tym klientach,
robotach itp. Celem libwww jest dostarczenie dobrze zoptymalizowanej,
przyk≥adowej implementacji HTTP, a takøe innych protoko≥Ûw
internetowych, oraz ∂rodowiska testowego do eksperymentÛw z
protoko≥ami.

%package devel
Summary:	Header files for programs that use libwww
Summary(pl):	Pliki nag≥Ûwkowe dla programÛw uøywaj±cych libwww
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files for libwww, which are available as public libraries.

%description devel -l pl
Pliki nag≥Ûwkowe dla libwww.

%package static
Summary:	Static libwww libraries
Summary(pl):	Statyczne biblioteki libwww
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static libwww libraries.

%description static -l pl
Statyczne biblioteki libwww.

%package apps
Summary:	Applications built using Libwww web library: e.g. Robot, command line tool, etc
Summary(pl):	Aplikacje uøywaj±ce Libwww: Robot, narzÍdzie command-line itp.
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
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
Aplikacje sieciowe zbudowane przy uøyciu libwww: Robot, narzÍdzie
comman-line, liniowa przegl±darka. Robot moøe przechodziÊ po stronach
szybciej i z mniejszym obci±øeniem niø inne znane roboty, dziÍki
wykorzystywaniu pipeliningu i HTTP/1.1. NarzÍdzie command-line (w3c)
jest uøyteczne do manipulowania serwisami WWW, ktÛre maj±
zaimplementowane co∂ wiÍcej niø HTTP GET (np. PUT, POST...).
Przegl±darka liniowa jest uøyteczna g≥Ûwnie do konwersji do zwyk≥ego
tekstu. Aktualnie niedostÍpna dopÛki kto∂ nie przystosuje jej do
nowego interfejsu (hint, hint...).

%prep
%setup -q
%patch0 -p1

%build
automake -a -c
%configure \
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
%{_datadir}/w3c-libwww

%files apps
%defattr(644,root,root,755)
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
