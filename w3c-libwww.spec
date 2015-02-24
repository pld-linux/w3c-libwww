Summary:	HTTP library of common code
Summary(pl.UTF-8):	Biblioteka wspólnego kodu HTTP
Summary(pt_BR.UTF-8):	Biblioteca HTTP de uso geral
Summary(ru.UTF-8):	HTTP-библиотека общеупотребительного кода
Summary(uk.UTF-8):	HTTP-бібліотека загальновживаного коду
Name:		w3c-libwww
Version:	5.4.0
Release:	19
License:	W3C (see: http://www.w3.org/Consortium/Legal/copyright-software.html)
Group:		Libraries
Source0:	http://www.w3.org/Library/Distribution/%{name}-%{version}.tgz
# Source0-md5:	c3734ca6caa405707e134cc8c6d7e422
Patch0:		%{name}-ac25x.patch
Patch1:		%{name}-system-expat.patch
Patch2:		%{name}-amfix.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-system-libmd5.patch
Patch5:		%{name}-ssl.patch
Patch6:		%{name}-nooldssl.patch
URL:		http://www.w3.org/Library/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libtool
BuildRequires:	libmd5-devel >= 20020413-2
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

%description -l pl.UTF-8
Libwww jest biblioteką WWW ogólnego przeznaczenia napisaną w C dla
Uniksów oraz Windows. Z wysoko rozszerzalnym i warstwowym API, może
mieć zastosowanie w wielu rodzajach aplikacji, w tym klientach,
robotach itp. Celem libwww jest dostarczenie dobrze zoptymalizowanej,
przykładowej implementacji HTTP, a także innych protokołów
internetowych, oraz środowiska testowego do eksperymentów z
protokołami.

%description -l pt_BR.UTF-8
A libwww é uma API web de propósito geral escrita em C para Unix e
Windows (Win32). Possui uma API altamente extensível e em camadas e
pode acomodar muitos tipos diferentes de aplicações, incluindo
clientes, robôs, etc. O propósito da libwww é fornecer uma
implementação HTTP exemplo altamente otimizada para servidor como um
ambiente de testes para experimentações com protocolos.

%description -l ru.UTF-8
Libwww - это Web API общего назначения, написанные на C для Unix и
Windows (Win32). Имея расширяемые многоуровневые API, она пригодна для
построения множества различных типов приложений включая клиентов,
роботов etc. Libwww является примером высокооптимизированной
реализации HTTP и других Интернет-протоколов и тестовой средой для
экспериментов с протоколами.

%description -l uk.UTF-8
Libwww - це Web API загального призначення, написані на C для Unix та
Windows (Win32). Маючи розширювані багаторівневі API, вона придатна
для побудови великої кількості різних різних типів прикладних програм
включаючи клієнтів, роботів etc. Libwww є прикладом
високооптимізованої реалізації HTTP та інших Інтернет-протоколів та
тестовим середовищем для експериментів з протоколами.

%package devel
Summary:	Header files for programs that use libwww
Summary(pl.UTF-8):	Pliki nagłówkowe dla programów używających libwww
Summary(pt_BR.UTF-8):	Arquivos necessários para desenvolvimento com a libwww
Summary(ru.UTF-8):	Библиотеки и хедеры для программ, которые используют libwww
Summary(uk.UTF-8):	Бібліотеки та хедери для програм, що використовують libwww
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel
Requires:	openssl-devel >= 0.9.7c
Requires:	zlib-devel

%description devel
Header files for libwww, which are available as public libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libwww.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento baseado na
libwww, que está disponível ao público.

%description devel -l ru.UTF-8
Библиотеки разработчика и хедеры для libwww.

%description devel -l uk.UTF-8
Бібліотеки програміста та хедери для libwww.

%package static
Summary:	Static libwww libraries
Summary(pl.UTF-8):	Statyczne biblioteki libwww
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com w3c-libwww
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwww libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libwww.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com w3c-libwww

%package apps
Summary:	Applications built using Libwww web library: e.g. Robot, command line tool, etc
Summary(pl.UTF-8):	Aplikacje używające Libwww: Robot, narzędzie command-line itp
Summary(pt_BR.UTF-8):	Aplicativos construídos usando a libwww
Summary(ru.UTF-8):	Приложения с использованием Libwww - робот, утилита командной строки и т.п.
Summary(uk.UTF-8):	Програми з використанням Libwww - робот, утиліта командного рядка і т.і.
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

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

%description apps -l pl.UTF-8
Aplikacje sieciowe zbudowane przy użyciu libwww: Robot, narzędzie
comman-line, liniowa przeglądarka. Robot może przechodzić po stronach
szybciej i z mniejszym obciążeniem niż inne znane roboty, dzięki
wykorzystywaniu pipeliningu i HTTP/1.1. Narzędzie command-line (w3c)
jest użyteczne do manipulowania serwisami WWW, które mają
zaimplementowane coś więcej niż HTTP GET (np. PUT, POST...).
Przeglądarka liniowa jest użyteczna głównie do konwersji do zwykłego
tekstu. Aktualnie niedostępna dopóki ktoś nie przystosuje jej do
nowego interfejsu (hint, hint...).

%description apps -l pt_BR.UTF-8
Aplicativos WEB utilizando a libwww: Robot, Ferramenta de execução de
linha de comando, navegação por linha de comando. Robot pode navegar
rapidamente e com baixa carga no sistema.

A Ferramenta de execução de linha de comando (w3c) é muito útil para
manipulação de sítios Web que implementam mais do que um HTTP GET (por
exemplo, PUT, POST, etc.)

%description apps -l ru.UTF-8
Web-приложения, построенные с использованием Libwww - робот, утилита
командной строки, строчный браузер. Робот может бродить по web-сайтам
быстрее и с меньшей нагрузкой чем любая другая известная нам бродилка
из-за исключительной конвейеризации и использования HTTP/1.1.

Утилита командной строки (w3c) очень полезна для работы с web-сайтами,
которые реализуют больше команд чем просто HTTP GET (например, PUT,
POST, etc.).

Строчный браузер - это минимальный web-браузер, работающий в командном
режиме. Часто полезен для преобразования в текстовый формат.

%description apps -l uk.UTF-8
Web-програми, побудовані з використанням Libwww - робот, утиліта
командної стрічки, командний браузер. Робот може ходити по web-сайтах
швидше та з меншим завантаженням ніж будь-яка відома нам ходилка
завдяки виключній конвейєризації та використанню HTTP/1.1.

Утиліта командного рядка (w3c) дуже корисна для роботи з web-сайтами,
які реалізують більше команд ніж просто HTTP GET (наприклад, PUT,
POST, etc.).

Командний браузер - це мінімальний web-браузер, що працює в командному
режимі. Часто корисний для перетворення у текстовий формат.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	ac_cv_lib_rx_regexec=no \
	--enable-shared \
	--with-dav \
	--with-gnu-ld \
	--with-md5 \
	--with-regex \
	--with-ssl \
	--with-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT.html ChangeLog LICENSE.html
%attr(755,root,root) %{_libdir}/libwww*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwww*.so.0
%attr(755,root,root) %{_libdir}/libpics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpics.so.0
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
%attr(755,root,root) %{_libdir}/libpics.so
%{_libdir}/libwww*.la
%{_libdir}/libpics.la
%{_includedir}/wwwconf.h
%{_includedir}/w3c-libwww

%files static
%defattr(644,root,root,755)
%{_libdir}/libwww*.a
%{_libdir}/libpics.a
