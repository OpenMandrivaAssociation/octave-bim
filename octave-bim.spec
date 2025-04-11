%global octpkg bim

Summary:	PDE Solver using a Finite Element/Finite Volume approach for Octave
Name:		octave-bim
Version:	1.1.6
Release:	3
License:	GPLv2+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/bim/
Url:		https://github.com/carlodefalco/bim
Source0:	https://github.com/carlodefalco/bim/archive/v%{version}/bim-%{version}.tar.gz
Patch0:		add-lacking-semicolon.patch

BuildRequires:  octave-devel >= 3.8.0
BuildRequires:  octave-fpl
BuildRequires:  octave-msh

Requires:	octave(api) = %{octave_api}
Requires:  	octave-fpl
Requires:  	octave-msh

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Package for solving Diffusion Advection Reaction (DAR) Partial
Differential Equations based on the Finite Volume Scharfetter-Gummel
(FVSG) method a.k.a Box Integration Method (BIM).

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
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

