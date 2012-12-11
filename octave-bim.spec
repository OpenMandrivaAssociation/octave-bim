%define	pkgname bim
%define name	octave-%{pkgname}
%define version 1.0.2
%define release %mkrel 1

Summary:	PAckage for solving DAR PDEs
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/actuarial/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.2.0
Requires:	octave-fpl >= 0.0.0
Requires:	octave-msh >= 0.0.0
BuildRequires:	octave-devel >= 3.2.0
BuildArch:	noarch

%description
Package for solving Diffusion Advection Reaction (DAR) Partial
Differential Equations based on the Finite Volume Scharfetter-Gummel
(FVSG) method a.k.a Box Integration Method (BIM).

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
rm -rf %{buildroot}
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean
%__rm -rf %{buildroot}

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}



%changelog
* Fri Dec 09 2011 Lev Givon <lev@mandriva.org> 1.0.2-1mdv2012.0
+ Revision: 739472
- Update to 1.0.2.

* Tue Jun 28 2011 Lev Givon <lev@mandriva.org> 1.0.1-1
+ Revision: 687746
- import octave-bim

