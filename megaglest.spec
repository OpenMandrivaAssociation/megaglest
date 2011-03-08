%define rev svn588
Name:		megaglest
Version:	3.4.0
Release:	%mkrel 1
Summary:	A free 3d real time strategy game
Summary(de):	Ein freies 3D Echtzeit-Strategiespiel
License:	GPLv2+
Group:		Games/Strategy
URL:		http://megaglest.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/megaglest/current_release/%{name}-source-%{version}.tar.xz
Source1:	%{name}.sh
Source2:	%{name}.png
Source3:	glest.ini
BuildRequires:	zlib-devel
BuildRequires:	openal-devel jpeg-devel
BuildRequires:	xerces-c-devel
BuildRequires:	SDL-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	Mesa-common-devel
BuildRequires:	jam
BuildRequires:	unzip
BuildRequires:	recode
BuildRequires:	lua-devel
BuildRequires:	libwxgtku-devel
Requires:	%{name}-data
Requires:	x11-font-adobe-utopia-75dpi
Requires:	mesa-demos
Requires: %{name}-data = %{version} 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
megaglest is a 3D OpenGL real time strategy game. It takes place in a 
context which could be compared to that of the pre-renaissance 
Europe, with the licence that magic forces exist in the environment 
and can be controlled.

%description -l de
megaglest ist ein 3D OpenGL-Echtzeit-Strategiespiel. Es findet in einem Zeitalter, 
man könnte die im Vergleich zu der vor-Renaissance Europa bezeichnen, in der 
magische Kräfte existieren und damit die Umwelt kontrolliert wird. Deep ruht 
Science in the Mindwie Magic tief im Herzen; Diese in der der Wille vorhanden 
ist stark, Diese wird Herrschaft in ihrem Namen.

%prep
%setup -q -n %{name}-source-%{version}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"

./autogen.sh
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir} \
	--enable-optimize

jam -d2 %{_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesbindir}
install -pm755 glest.bin %{buildroot}%{_gamesbindir}/%{name}-bin
install -m755 %{SOURCE1} -D %{buildroot}%{_gamesbindir}/%{name}

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}/{data/lang,maps}
install -m644 %{SOURCE3} %{buildroot}%{_gamesdatadir}/%{name}
install -m644 glestkeys.ini %{buildroot}%{_gamesdatadir}/%{name}

mkdir -p %{buildroot}%{_iconsdir}
install -m644 %{SOURCE2} -D %{buildroot}%{_iconsdir}/%{name}.png

# Desktop file
mkdir -p %{buildroot}/%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/megaglest.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Real Time Strategy game
Comment[de]=Echtzeit-Strategiespiel
Exec=%{_gamesbindir}/%{name}
Icon=megaglest.png
StartupNotify=true
Terminal=false
Type=Application
Categories=Game;StrategyGame;X-MandrivaLinux-MoreApplications-Games-Strategy;
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamesbindir}/*
%{_iconsdir}/%{name}.png
%{_datadir}/applications/*
%{_gamesdatadir}/%{name}

