%define module  GIFgraph
%define name	perl-%{module}
%define version 1.20
%define release %mkrel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Graph Plotting Module (deprecated) 
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{module}/
Source:	    http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{module}-%{version}.tar.gz
BuildRequires:	perl(GD::Graph)
BuildRequires:	perl(Image::Magick)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GIFgraph is a perl5 module to create and display GIF output for a graph.

GIFgraph is nothing more than a wrapper around GD::Graph, and its use is
deprecated. It only exists for backward compatibility. The documentation for
all the functionality can be found in GD::Graph

%prep
%setup -q -n %{module}-%{version} 

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

