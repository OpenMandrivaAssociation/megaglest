Name:		megaglest
Version:	3.6.0.2
Release:	%mkrel 0.1
Summary:	Open Source 3d real time strategy game
License:	GPLv3+
Group:		Games/Strategy
Url:		http://megaglest.org/
Source0:	http://sourceforge.net/projects/megaglest/files/megaglest_3.6.0.2/megaglest-source-3.6.0.2.tar.xz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	GL-devel
BuildRequires:	ftgl-devel
BuildRequires:	glew-devel
BuildRequires:	gnutls-devel
BuildRequires:	icu-devel
BuildRequires:	jpeg-devel
BuildRequires:	libircclient-static-devel
BuildRequires:	lua-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	openal-devel
BuildRequires:	png-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	subversion
BuildRequires:	xerces-c28-devel
BuildRequires:	wxgtku-devel
BuildRequires:	x11-server-xvfb
BuildRequires:	zlib-devel
Requires:	glxinfo
Requires:	megaglest-data
Requires:	p7zip

Patch0:		megaglest-3.6.0.1-noerror.patch
Patch1:		megaglest-3.6.0.2-help2man.patch

%description
MegaGlest is an open source 3D-real-time strategy game, where you control
the armies of one of seven different factions: Tech, Magic, Egyptians,
Indians, Norsemen, Persian or Romans. The game is setup in one of 16
naturally looking settings, which -like the unit models- are crafted with
great appreciation for detail. Additional game data can be downloaded from
within the game at no cost.

#-----------------------------------------------------------------------
%prep
%setup -q

%patch0 -p1
%patch1 -p1

#-----------------------------------------------------------------------
%build
%cmake									\
	-DCMAKE_INSTALL_PREFIX=/					\
	-DMEGAGLEST_BIN_INSTALL_PATH=%{_gamesbindir}			\
	-DMEGAGLEST_ICON_INSTALL_PATH=%{_iconsdir}			\
	-DMEGAGLEST_DATA_INSTALL_PATH=%{_gamesdatadir}/megaglest
%make

#-----------------------------------------------------------------------
%install
%makeinstall_std -C build
mv %{buildroot}/share/* %{buildroot}%{_datadir}
rmdir %{buildroot}/share

#-----------------------------------------------------------------------
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamesbindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/*
%{_mandir}/man6/*.6*
