Summary:	HTTP library of common code
Summary(pl):	Biblioteka wspólnego kodu HTTP
Summary(pt_BR):	Biblioteca HTTP de uso geral
Name:		w3c-libwww
Version:	5.3.2
Release:	7
License:	W3C (see: http://www.w3.org/Consortium/Legal/copyright-software.html)
Group:		Libraries
Source0:	http://www.w3.org/Library/Distribution/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac25x.patch
Patch1:		%{name}-am15.patch
Patch2:		%{name}-system-expat.patch
Icon:		Lib48x.gif
URL:		http://www.w3.org/Library/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	zlib-devel
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

%description -l pt_BR
A libwww é uma API web de propósito geral escrita em C para Unix e
Windows (Win32). Possui uma API altamente extensível e em camadas e
pode acomodar muitos tipos diferentes de aplicações, incluindo
clientes, robôs, etc. O propósito da libwww é fornecer uma
implementação HTTP exemplo altamente otimizada para servidor como um
ambiente de testes para experimentações com protocolos.

%package devel
Summary:	Header files for programs that use libwww
Summary(pl):	Pliki nag³ówkowe dla programów u¿ywaj±cych libwww
Summary(pt_BR):	Arquivos necessários para desenvolvimento com a libwww
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libwww, which are available as public libraries.

%description devel -l pl
Pliki nag³ówkowe dla libwww.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento baseado na
libwww, que está disponível ao público.

%package static
Summary:	Static libwww libraries
Summary(pl):	Statyczne biblioteki libwww
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com w3c-libwww
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libwww libraries.

%description static -l pl
Statyczne biblioteki libwww.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com w3c-libwww

%package apps
Summary:	Applications built using Libwww web library: e.g. Robot, command line tool, etc
Summary(pl):	Aplikacje u¿ywaj±ce Libwww: Robot, narzêdzie command-line itp
Summary(pt_BR):	Aplicativos construídos usando a libwww
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

%description apps -l pt_BR
Aplicativos WEB utilizando a libwww: Robot, Ferramenta de execução de
linha de comando, navegação por linha de comando. Robot pode navegar
rapidamente e com baixa carga no sistema.

A Ferramenta de execução de linha de comando (w3c) é muito útil para
manipulação de sítios Web que implementam mais do que um HTTP GET (por
exemplo, PUT, POST, etc.)

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--with-gnu-ld \
	--with-md5 \
	--with-regex \
	--with-ssl \
	--with-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__mkdir} documentation
%{__cp} -p --parents *.html */*.html */*/*.html documentation

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc documentation/* Icons/*/*.gif
%attr(755,root,root) %{_libdir}/libwww*.so.*.*
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
%attr(755,root,root) %{_libdir}/libmd5.so
%attr(755,root,root) %{_libdir}/libpics.so
%{_libdir}/libwww*.la
%{_libdir}/libmd5.la
%{_libdir}/libpics.la

%{_includedir}/wwwconf.h
%{_includedir}/w3c-libwww

%files static
%defattr(644,root,root,755)
%{_libdir}/libwww*.a
%{_libdir}/libmd5.a
%{_libdir}/libpics.a
