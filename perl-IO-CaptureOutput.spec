#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	IO
%define	pnam	CaptureOutput
Summary:	IO::CaptureOutput - capture STDOUT and STDERR from Perl code, subprocesses or XS
Summary(pl.UTF-8):	IO::CaptureOutput - przechwytywanie STDOUT i STDERR z kodu w Perlu, podprocesów lub XS
Name:		perl-IO-CaptureOutput
Version:	1.1104
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5c98f4ed8e6aa5237e610b5865f275e9
URL:		http://search.cpan.org/dist/IO-CaptureOutput/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 3.27
BuildRequires:	perl-File-Temp >= 0.16
BuildRequires:	perl-Test-Simple >= 0.62
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides routines for capturing STDOUT and STDERR from
perl subroutines, forked system calls (e.g. system(), fork()) and from
XS or C modules.

%description -l pl.UTF-8
Ten moduł udostępnia procedury do przechwytywania STDOUT i STDERR z
funkcji perlowych, odgałęzionych wywołań systemowych (np. system(),
fork()) oraz z modułów XS lub C.

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
%{perl_vendorlib}/IO/CaptureOutput.pm
%{_mandir}/man3/IO::CaptureOutput.3pm*
%{_examplesdir}/%{name}-%{version}
