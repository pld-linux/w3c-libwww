# Note that this is NOT a relocatable package

%define ver	5.2.8
%define rel	3
%define prefix	/usr/

Summary: HTTP library of common code
Name: w3c-libwww
Version: %ver
Release: %rel
Copyright: W3C (see: http://www.w3.org/Consortium/Legal/copyright-software.html)
Group: System Environment/Libraries
Source: http://www.w3.org/Library/Distribution/w3c-libwww-%{ver}.tar.gz
URL: http://www.w3.org/Library
BuildRoot: /var/tmp/%{name}-root
Icon: Lib48x.gif

%description
Libwww is a general-purpose Web API written in C for Unix and Windows (Win32).
With a highly extensible and layered API, it can accommodate many different
types of applications including clients, robots, etc. The purpose of libwww
is to provide a highly optimized HTTP sample implementation as well as other
Internet protocols and to serve as a testbed for protocol experiments.

%package devel
Summary: Libraries and header files for programs that use libwww.
Group: Development/Libraries
Requires: w3c-libwww

%description devel
Static libraries and header files for libwww, which are available as public
libraries.

%package apps
Summary: Applications built using Libwww web library: e.g. Robot, command line tool, etc.
Group: Applications/Internet
Requires: w3c-libwww
Icon: robot48x.gif

%description apps

Web applications built using Libwww: Robot, Command line tool, 
line mode browser.  The Robot can crawl web sites faster, and
with lower load, than any other web walker that we know of, 
due to its extensive pipelining and use of HTTP/1.1.

The command line tool (w3c) is very useful for manipulation of 
Web sites that implement more than just HTTP GET (e.g. PUT, 
 POST, etc.).

The line mode browser is a minimal line mode web browser; 
often useful to convert to ascii text.  Currently unavailable
until someone updates it to some new interfaces. (hint, hint...)

%prep
%setup -q

%build
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --with-regex --with-zlib
#make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%configure --enable-shared --with-gnu-ld --with-regex --with-zlib
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

( cd $RPM_BUILD_ROOT
  chmod +x ./usr/lib/lib{www*,xml*,md5}.so.0.*
  strip ./usr/bin/* || :
)

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{prefix}/lib/libwww*.so.*
%{prefix}/lib/libxml*.so.*
%{prefix}/lib/libmd5.so.*
%{prefix}/share/w3c-libwww

%doc *.html */*.html */*/*.html Icons/*/*.gif

%files apps
%defattr(-,root,root)
%{prefix}/bin/webbot
%{prefix}/bin/w3c

%files devel
%defattr(-,root,root)
%{prefix}/bin/libwww-config
%{prefix}/lib/lib*.a
%{prefix}/lib/lib*.la
%{prefix}/lib/lib*.so

%{prefix}/include/xmlparse.h
%{prefix}/include/w3c-libwww
