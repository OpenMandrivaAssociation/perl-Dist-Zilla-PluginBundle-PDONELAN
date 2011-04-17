%define upstream_name    Dist-Zilla-PluginBundle-PDONELAN
%define upstream_version 1.101750

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Dist::Zilla plugin bundle for PDONELAN
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla::PluginBundle::Filter)
BuildRequires: perl(Dist::Zilla::PluginBundle::Git)
BuildRequires: perl(Dist::Zilla::Role::PluginBundle)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Test::More)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangeLog)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangesTests)
BuildRequires: perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires: perl(Dist::Zilla::Plugin::DistManifestTests)
BuildRequires: perl(Dist::Zilla::Plugin::HasVersionTests)
BuildRequires: perl(Dist::Zilla::Plugin::MinimumVersionTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::PortabilityTests)
BuildRequires: perl(Dist::Zilla::Plugin::Prepender)
BuildRequires: perl(Dist::Zilla::Plugin::ReadmeFromPod)
BuildRequires: perl(Module::Build) >= 0.3601
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE META.json README
%{_mandir}/man3/*
%perl_vendorlib/*


