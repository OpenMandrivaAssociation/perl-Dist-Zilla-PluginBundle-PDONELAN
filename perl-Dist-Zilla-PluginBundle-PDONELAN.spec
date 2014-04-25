%define upstream_name    Dist-Zilla-PluginBundle-PDONELAN
%define upstream_version 1.201

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Dist::Zilla plugin bundle for PDONELAN

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Dist::Zilla::Plugin::UpdateGitHub)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangesHasContent)
BuildRequires: perl(Dist::Zilla::Plugin::GithubMeta)
BuildRequires: perl(Dist::Zilla::Plugin::MinimumPerl)
BuildRequires: perl(Dist::Zilla::Plugin::EOLTests)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Filter)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Git)
BuildRequires:	perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Dist::Zilla::Plugin::CheckChangeLog)
BuildRequires:	perl(Dist::Zilla::Plugin::CheckChangesTests)
BuildRequires:	perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires:	perl(Dist::Zilla::Plugin::DistManifestTests)
BuildRequires:	perl(Dist::Zilla::Plugin::HasVersionTests)
BuildRequires:	perl(Dist::Zilla::Plugin::MinimumVersionTests)
BuildRequires:	perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires:	perl(Dist::Zilla::Plugin::PortabilityTests)
BuildRequires:	perl(Dist::Zilla::Plugin::Prepender)
BuildRequires:	perl(Dist::Zilla::Plugin::ReadmeFromPod)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
Dist::Zilla plugin bundle for PDONELAN

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*


