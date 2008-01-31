Summary:	Extract iso9660 image from device or file
Summary(pl.UTF-8):	Tworzenie obrazów iso9660 z urządzenia lub pliku
Name:		isodump
Version:	0.06.00
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://linux.xulin.de/c/%{name}-%{version}.tar.gz
# Source0-md5:	da6996e1c3e8abc5de0904b232e379e0
Patch0:		%{name}-Makefile.patch
URL:		http://linux.xulin.de/c/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line utility to extract iso9660 image from device or file.

%description -l pl.UTF-8
Narzędzie wiersza poleceń do tworzenia obrazów iso9660 z
urządzenia lub pliku.

%prep
%setup -q
%patch0 -p1

%build
./configure
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/isodump
%{_mandir}/man1/isodump.1*
