Name:           noiz2sa
Version:        0.51a
Release:        %mkrel 1
Summary:        Abstract arcade shooter
License:        BSD
Group:          Games/Arcade
URL:            http://noiz2sa.sourceforge.net/
Source0:        http://downloads.sourceforge.net/noiz2sa/noiz2sa-%{version}.tar.gz
Source1:        noiz2sa.6
Source2:        noiz2sa.desktop
Source3:        noiz2sa.xpm
Source4:        copyright
Patch0:         noiz2sa-0.51a.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  bison
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel

%description
A classical vertical arcade shooter with an abstract theme and
matching electronic music.

Screenshot:
http://noiz2sa.sourceforge.net/noiz2sa_screen.png

%prep
%setup -q -n %{name}
%patch0 -p1
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .

%build
cd src && make -f makefile.lin

%install
rm -rf %{buildroot}

install -d %{buildroot}/%{_gamesbindir}/
install -m 0755 src/noiz2sa %{buildroot}/%{_gamesbindir}/

install -d %{buildroot}/%{_datadir}/games/
cp -R noiz2sa_share/ %{buildroot}/%{_datadir}/games/noiz2sa/

install -d %{buildroot}%{_mandir}/man6/
install -m 0644 noiz2sa.6 %{buildroot}%{_mandir}/man6/

install -d %{buildroot}%{_datadir}/noiz2sa/
install -m 0644 noiz2sa.xpm %{buildroot}%{_datadir}/noiz2sa/

install -d %{buildroot}%{_datadir}/applications/
install -m 0644 noiz2sa.desktop %{buildroot}%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc copyright
%{_gamesbindir}/noiz2sa
%{_datadir}/games/noiz2sa/
%{_mandir}/man6/noiz2sa.6*
%{_datadir}/applications/noiz2sa.desktop
%{_datadir}/noiz2sa/
%{_datadir}/noiz2sa/noiz2sa.xpm
