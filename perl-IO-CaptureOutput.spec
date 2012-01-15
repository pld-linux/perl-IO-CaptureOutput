#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	CaptureOutput
Summary:	IO::CaptureOutput - capture STDOUT and STDERR from Perl code, subprocesses or XS
#Summary(pl.UTF-8):	
Name:		perl-IO-CaptureOutput
Version:	1.1102
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	367b3c0eb33a4b600de4009b0445ae0d
URL:		http://search.cpan.org/dist/IO-CaptureOutput/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Spec >= 3.27
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides routines for capturing STDOUT and STDERR from
perl subroutines, forked system calls (e.g. system(), fork()) and from
XS or C modules.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/IO/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
