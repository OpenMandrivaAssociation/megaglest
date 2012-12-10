# no matter what, ignores -lssl -lcrypto dependency of -lcurl
%define		_disable_ld_as_needed		1

Name:		megaglest
Version:	3.6.0.3
Release:	2
Summary:	Open Source 3d real time strategy game
License:	GPLv3+
Group:		Games/Strategy
Url:		http://megaglest.org/
Source0:	http://sourceforge.net/projects/megaglest/files/%{name}_%{version}/%{name}-source-%{version}.tar.xz
Patch0:		megaglest-3.6.0.1-noerror.patch
Patch1:		megaglest-3.6.0.2-help2man.patch
Patch2:		megaglest-3.6.0.3-underlink.patch
Patch3:		megaglest-3.6.0.3-gcc47.patch

BuildRequires:	cmake
BuildRequires:	help2man
BuildRequires:	subversion
BuildRequires:	x11-server-xvfb
BuildRequires:	icu-devel
BuildRequires:	jpeg-devel
BuildRequires:	libircclient-static-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	wxgtku-devel
BuildRequires:	xerces-c28-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ftgl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)
Requires:	glxinfo
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

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
install -d %{buildroot}%{_gamesdatadir}/megaglest
for image in `ls %{buildroot}%{_iconsdir}`; do
    [ -e %{buildroot}%{_gamesdatadir}/$image ] ||
	ln -sf %{_iconsdir}/$image %{buildroot}%{_gamesdatadir}/megaglest
done
# installed by megaglest-data
rm %{buildroot}%{_gamesdatadir}/megaglest/megaglest.bmp

#-----------------------------------------------------------------------
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamesbindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/*
%{_mandir}/man6/*.6*
%{_gamesdatadir}/megaglest

