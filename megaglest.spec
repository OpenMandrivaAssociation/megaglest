Name:		megaglest
Version:	3.5.2.4
Release:	1
Summary:	Open Source 3d real time strategy game
License:	GPLv3+
Group:		Games/Strategy
Url:		http://megaglest.org/
Source0:	http://sourceforge.net/projects/megaglest/files/current_release/megaglest-source-3.5.2.4.tar.xz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	cmake
BuildRequires:	GL-devel
BuildRequires:	gnutls-devel
BuildRequires:	icu-devel
BuildRequires:	jpeg-devel
BuildRequires:	lua-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	openal-devel
BuildRequires:	png-devel
BuildRequires:	SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	xerces-c28-devel
BuildRequires:	wxgtku-devel
BuildRequires:	zlib-devel
Requires:	gxlinfo
Requires:	megaglest-data
Requires:	p7zip

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
%{_mandir}/man6/%{name}.6*
