%global octpkg bim

Summary:	PDE Solver using a Finite Element/Finite Volume approach for Octave
Name:		octave-%{octpkg}
Version:	1.1.5
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?44883
Patch0:		add-lacking-semicolon.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.8.0
BuildRequires:	octave-fpl
BuildRequires:	octave-msh

Requires:	octave(api) = %{octave_api}
Requires:	octave-fpl
Requires:	octave-msh

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Package for solving Diffusion Advection Reaction (DAR) Partial
Differential Equations based on the Finite Volume Scharfetter-Gummel
(FVSG) method a.k.a Box Integration Method (BIM).

This package is part of external Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

