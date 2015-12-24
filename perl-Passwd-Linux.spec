#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Passwd
%define	pnam	Linux
Summary:	Passwd::Linux - Perl module for manipulating the passwd and shadow files
Summary(pl.UTF-8):	Passwd::Linux - Moduł Perla do manipulowania plikami passwd i shadow
Name:		perl-Passwd-Linux
Version:	0.70
Release:	9
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/E/EE/EESTABROO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f7901ab4706366d8cb9c8fd43e167072
URL:		http://search.cpan.org/dist/Passwd-Linux/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Passwd::Linux provides additional password routines. It augments the
getpw* functions with setpwinfo, modpwinfo, rmpwnam, mgetpwnam. You
need to run most of the functions as root or as someone who has
permission to modify the shadow file.

%description -l pl.UTF-8
Passwd::Linux dostarcza dodatkowych metod obsługi haseł. Powiększa
funkcje getpw* o setpwinfo, modpwinfo, rmpwnam, mgetpwnam. Większość
tych funkcji musi być uruchomiona z uprawnieniami roota lub osoby
mającej uprawnienia do modyfikacji pliku shadow.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Passwd/Linux/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorarch}/Passwd
%{perl_vendorarch}/Passwd/*.pm
%dir %{perl_vendorarch}/auto/Passwd
%dir %{perl_vendorarch}/auto/Passwd/Linux
%{perl_vendorarch}/auto/Passwd/Linux/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Passwd/Linux/*.so
%{_mandir}/man3/*
