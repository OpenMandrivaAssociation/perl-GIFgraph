%define upstream_name    GIFgraph
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Graph Plotting Module (deprecated) 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(GD::Graph)
BuildRequires:	perl(Image::Magick)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot} 
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/GIFgraph.pm
%{perl_vendorlib}/GIFgraph/
%{_mandir}/*/*
