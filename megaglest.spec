# no matter what, ignores -lssl -lcrypto dependency of -lcurl
%define		_disable_ld_as_needed		1
%define		_disable_lto 1

%define		debug_package			%{nil}

Name:		megaglest
Version:	3.12.0
Release:	1
Summary:	Open Source 3d real time strategy game
License:	GPLv3+
Group:		Games/Strategy
Url:		http://megaglest.org/
Source0:	https://github.com/MegaGlest/megaglest-source/releases/download/%{version}/%{name}-source-%{version}.tar.xz
# Correct usage of xvfb-run when generating manpages
Patch0:		%{name}-help2man.patch
# Do not fail with cryptic message if there are missing translations
# just use english text
Patch1:		%{name}-translation-missing.patch
# Use proper path to g3dviewer.ico in sources
#Patch2:         %{name}-icon-path.patch
# Mandriva patch
#Patch3:		%{name}-underlink.patch
#Patch4:		megaglest-source-3.11.1_cmake3.2-x11.patch

BuildRequires:	cmake
BuildRequires:	help2man
BuildRequires:	subversion
BuildRequires:	x11-server-xvfb
BuildRequires:	icu-devel
BuildRequires:	jpeg-devel
BuildRequires:	libircclient-static-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	wxgtku3.0-devel
BuildRequires:	xerces-c-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ftgl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_net)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)
Requires:	glxinfo
Requires:	megaglest-data = %{version}
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

%apply_patches

#-----------------------------------------------------------------------
%build
export CC=gcc
export CXX=g++
sed -i -e 's/-O3//g' `find . -name CMakeLists.txt`
%cmake									\
-DMEGAGLEST_BIN_INSTALL_PATH=games/ \
       -DMEGAGLEST_DATA_INSTALL_PATH=share/games/%{name}/

%make

#-----------------------------------------------------------------------
%install
%makeinstall_std -C build

#-----------------------------------------------------------------------
%files
%doc docs/AUTHORS.source_code.txt
%doc docs/CHANGELOG.txt
%doc docs/COPYRIGHT.source_code.txt
%doc docs/gnu_gpl_3.0.txt
%doc docs/README.txt
%{_mandir}/man6/*.6*
%{_gamesbindir}/*
%{_gamesdatadir}/megaglest/*
