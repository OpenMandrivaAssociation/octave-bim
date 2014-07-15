%define	pkgname bim

Summary:	Package for solving DAR PDEs
Name:		octave-%{pkgname}
Version:	1.0.2
Release:	2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/actuarial/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.2.0
Requires:	octave-fpl >= 0.0.0
Requires:	octave-msh >= 0.0.0
BuildRequires:	octave-devel >= 3.2.0
BuildArch:	noarch
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Package for solving Diffusion Advection Reaction (DAR) Partial
Differential Equations based on the Finite Volume Scharfetter-Gummel
(FVSG) method a.k.a Box Integration Method (BIM).

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %{SOURCE0} 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}



