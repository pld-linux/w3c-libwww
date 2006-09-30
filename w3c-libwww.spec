Summary:	HTTP library of common code
Summary(pl):	Biblioteka wspСlnego kodu HTTP
Summary(pt_BR):	Biblioteca HTTP de uso geral
Summary(ru):	HTTP-библиотека общеупотребительного кода
Summary(uk):	HTTP-б╕бл╕отека загальновживаного коду
Name:		w3c-libwww
Version:	5.4.0
Release:	5
License:	W3C (see: http://www.w3.org/Consortium/Legal/copyright-software.html)
Group:		Libraries
Source0:	http://www.w3.org/Library/Distribution/%{name}-%{version}.tgz
# Source0-md5:	c3734ca6caa405707e134cc8c6d7e422
Patch0:		%{name}-ac25x.patch
Patch1:		%{name}-am15.patch
Patch2:		%{name}-system-expat.patch
Patch3:		%{name}-amfix.patch
URL:		http://www.w3.org/Library/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
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
Libwww jest bibliotek╠ WWW ogСlnego przeznaczenia napisan╠ w C dla
UniksСw oraz Windows. Z wysoko rozszerzalnym i warstwowym API, mo©e
mieФ zastosowanie w wielu rodzajach aplikacji, w tym klientach,
robotach itp. Celem libwww jest dostarczenie dobrze zoptymalizowanej,
przykЁadowej implementacji HTTP, a tak©e innych protokoЁСw
internetowych, oraz ╤rodowiska testowego do eksperymentСw z
protokoЁami.

%description -l pt_BR
A libwww И uma API web de propСsito geral escrita em C para Unix e
Windows (Win32). Possui uma API altamente extensМvel e em camadas e
pode acomodar muitos tipos diferentes de aplicaГУes, incluindo
clientes, robТs, etc. O propСsito da libwww И fornecer uma
implementaГЦo HTTP exemplo altamente otimizada para servidor como um
ambiente de testes para experimentaГУes com protocolos.

%description -l ru
Libwww - это Web API общего назначения, написанные на C для Unix и
Windows (Win32). Имея расширяемые многоуровневые API, она пригодна для
построения множества различных типов приложений включая клиентов,
роботов etc. Libwww является примером высокооптимизированной
реализации HTTP и других Интернет-протоколов и тестовой средой для
экспериментов с протоколами.

%description -l uk
Libwww - це Web API загального призначення, написан╕ на C для Unix та
Windows (Win32). Маючи розширюван╕ багатор╕внев╕ API, вона придатна
для побудови велико╖ к╕лькост╕ р╕зних р╕зних тип╕в прикладних програм
включаючи кл╕╓нт╕в, робот╕в etc. Libwww ╓ прикладом
високооптим╕зовано╖ реал╕зац╕╖ HTTP та ╕нших ╤нтернет-протокол╕в та
тестовим середовищем для експеримент╕в з протоколами.

%package devel
Summary:	Header files for programs that use libwww
Summary(pl):	Pliki nagЁСwkowe dla programСw u©ywaj╠cych libwww
Summary(pt_BR):	Arquivos necessАrios para desenvolvimento com a libwww
Summary(ru):	Библиотеки и хедеры для программ, которые используют libwww
Summary(uk):	Б╕бл╕отеки та хедери для програм, що використовують libwww
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	expat-devel
Requires:	openssl-devel >= 0.9.7c
Requires:	zlib-devel

%description devel
Header files for libwww, which are available as public libraries.

%description devel -l pl
Pliki nagЁСwkowe dla libwww.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusЦo para desenvolvimento baseado na
libwww, que estА disponМvel ao pЗblico.

%description devel -l ru
Библиотеки разработчика и хедеры для libwww.

%description devel -l uk
Б╕бл╕отеки програм╕ста та хедери для libwww.

%package static
Summary:	Static libwww libraries
Summary(pl):	Statyczne biblioteki libwww
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com w3c-libwww
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libwww libraries.

%description static -l pl
Statyczne biblioteki libwww.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com w3c-libwww

%package apps
Summary:	Applications built using Libwww web library: e.g. Robot, command line tool, etc
Summary(pl):	Aplikacje u©ywaj╠ce Libwww: Robot, narzЙdzie command-line itp
Summary(pt_BR):	Aplicativos construМdos usando a libwww
Summary(ru):	Приложения с использованием Libwww - робот, утилита командной строки и т.п.
Summary(uk):	Програми з використанням Libwww - робот, утил╕та командного рядка ╕ т.╕.
Group:		Applications/Networking
Requires:	%{name} = %{version}

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
Aplikacje sieciowe zbudowane przy u©yciu libwww: Robot, narzЙdzie
comman-line, liniowa przegl╠darka. Robot mo©e przechodziФ po stronach
szybciej i z mniejszym obci╠©eniem ni© inne znane roboty, dziЙki
wykorzystywaniu pipeliningu i HTTP/1.1. NarzЙdzie command-line (w3c)
jest u©yteczne do manipulowania serwisami WWW, ktСre maj╠
zaimplementowane co╤ wiЙcej ni© HTTP GET (np. PUT, POST...).
Przegl╠darka liniowa jest u©yteczna gЁСwnie do konwersji do zwykЁego
tekstu. Aktualnie niedostЙpna dopСki kto╤ nie przystosuje jej do
nowego interfejsu (hint, hint...).

%description apps -l pt_BR
Aplicativos WEB utilizando a libwww: Robot, Ferramenta de execuГЦo de
linha de comando, navegaГЦo por linha de comando. Robot pode navegar
rapidamente e com baixa carga no sistema.

A Ferramenta de execuГЦo de linha de comando (w3c) И muito Зtil para
manipulaГЦo de sМtios Web que implementam mais do que um HTTP GET (por
exemplo, PUT, POST, etc.)

%description apps -l ru
Web-приложения, построенные с использованием Libwww - робот, утилита
командной строки, строчный браузер. Робот может бродить по web-сайтам
быстрее и с меньшей нагрузкой чем любая другая известная нам бродилка
из-за исключительной конвейеризации и использования HTTP/1.1.

Утилита командной строки (w3c) очень полезна для работы с web-сайтами,
которые реализуют больше команд чем просто HTTP GET (например, PUT,
POST, etc.).

Строчный браузер - это минимальный web-браузер, работающий в командном
режиме. Часто полезен для преобразования в текстовый формат.

%description apps -l uk
Web-програми, побудован╕ з використанням Libwww - робот, утил╕та
командно╖ стр╕чки, командний браузер. Робот може ходити по web-сайтах
швидше та з меншим завантаженням н╕ж будь-яка в╕дома нам ходилка
завдяки виключн╕й конвей╓ризац╕╖ та використанню HTTP/1.1.

Утил╕та командного рядка (w3c) дуже корисна для роботи з web-сайтами,
як╕ реал╕зують б╕льше команд н╕ж просто HTTP GET (наприклад, PUT,
POST, etc.).

Командний браузер - це м╕н╕мальний web-браузер, що працю╓ в командному
режим╕. Часто корисний для перетворення у текстовий формат.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT.html ChangeLog LICENSE.html
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
