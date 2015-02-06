%define upstream_name    GIFgraph
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Graph Plotting Module (deprecated) 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(GD::Graph)
BuildRequires:	perl(Image::Magick)
BuildArch:	noarch

%description
GIFgraph is a perl5 module to create and display GIF output for a graph.

GIFgraph is nothing more than a wrapper around GD::Graph, and its use is
deprecated. It only exists for backward compatibility. The documentation for
all the functionality can be found in GD::Graph

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%install
%makeinstall_std

%check
make test

%files
%doc README
%{perl_vendorlib}/GIFgraph.pm
%{perl_vendorlib}/GIFgraph/
%{_mandir}/*/*


%changelog
* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.0
+ Revision: 410069
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.20-3mdv2009.0
+ Revision: 257105
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.20-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2008.0
+ Revision: 82192
- import perl-GIFgraph


* Sat Sep 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2008.0
- first mdv release 
