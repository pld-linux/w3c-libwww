Summary:	HTTP library of common code
Summary(pl):	Biblioteka wsp�lnego kodu HTTP
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
Libwww jest bibliotek� WWW og�lnego przeznaczenia napisan� w C dla
Uniks�w oraz Windows. Z wysoko rozszerzalnym i warstwowym API, mo�e
mie� zastosowanie w wielu rodzajach aplikacji, w tym klientach,
robotach itp. Celem libwww jest dostarczenie dobrze zoptymalizowanej,
przyk�adowej implementacji HTTP, a tak�e innych protoko��w
internetowych, oraz �rodowiska testowego do eksperyment�w z
protoko�ami.

%description -l pt_BR
A libwww � uma API web de prop�sito geral escrita em C para Unix e
Windows (Win32). Possui uma API altamente extens�vel e em camadas e
pode acomodar muitos tipos diferentes de aplica��es, incluindo
clientes, rob�s, etc. O prop�sito da libwww � fornecer uma
implementa��o HTTP exemplo altamente otimizada para servidor como um
ambiente de testes para experimenta��es com protocolos.

%package devel
Summary:	Header files for programs that use libwww
Summary(pl):	Pliki nag��wkowe dla program�w u�ywaj�cych libwww
Summary(pt_BR):	Arquivos necess�rios para desenvolvimento com a libwww
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libwww, which are available as public libraries.

%description devel -l pl
Pliki nag��wkowe dla libwww.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento baseado na
libwww, que est� dispon�vel ao p�blico.

%package static
Summary:	Static libwww libraries
Summary(pl):	Statyczne biblioteki libwww
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com w3c-libwww
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libwww libraries.

%description static -l pl
Statyczne biblioteki libwww.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com w3c-libwww

%package apps
Summary:	Applications built using Libwww web library: e.g. Robot, command line tool, etc
Summary(pl):	Aplikacje u�ywaj�ce Libwww: Robot, narz�dzie command-line itp
Summary(pt_BR):	Aplicativos constru�dos usando a libwww
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
Aplikacje sieciowe zbudowane przy u�yciu libwww: Robot, narz�dzie
comman-line, liniowa przegl�darka. Robot mo�e przechodzi� po stronach
szybciej i z mniejszym obci��eniem ni� inne znane roboty, dzi�ki
wykorzystywaniu pipeliningu i HTTP/1.1. Narz�dzie command-line (w3c)
jest u�yteczne do manipulowania serwisami WWW, kt�re maj�
zaimplementowane co� wi�cej ni� HTTP GET (np. PUT, POST...).
Przegl�darka liniowa jest u�yteczna g��wnie do konwersji do zwyk�ego
tekstu. Aktualnie niedost�pna dop�ki kto� nie przystosuje jej do
nowego interfejsu (hint, hint...).

%description apps -l pt_BR
Aplicativos WEB utilizando a libwww: Robot, Ferramenta de execu��o de
linha de comando, navega��o por linha de comando. Robot pode navegar
rapidamente e com baixa carga no sistema.

A Ferramenta de execu��o de linha de comando (w3c) � muito �til para
manipula��o de s�tios Web que implementam mais do que um HTTP GET (por
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
