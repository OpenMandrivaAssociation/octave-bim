%define octpkg bim

Summary:	Package for solving DAR PDEs with Octave
Name:		octave-%{octpkg}
Version:	1.1.5
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.8.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-fpl
Requires:	octave-msh 

Requires(post): octave
Requires(postun): octave

%description
Package for solving Diffusion Advection Reaction (DAR) Partial
Differential Equations based on the Finite Volume Scharfetter-Gummel
(FVSG) method a.k.a Box Integration Method (BIM).


This package is part of external Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

