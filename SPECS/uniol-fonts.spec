# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/font-uniol
%global tag 1
Source0: {forgesource}
Source1: https://github.com/mitradranirban/uniol-fonts/raw/main/SOURCE/66-0-uniol-fonts.conf
Source2: https://github.com/mitradranirban/uniol-fonts/raw/main/SOURCE/generate.pe
Version:   1.0.0
Release:   2%{dist}
URL: %{forgeurl}
%global fontfamily    uniol        
%global fontlicense       OFL
%global fontlicenses      LICENCE
%global fontdocs       README.md   
%global fontdocsex        %{fontlicenses}
%global fontsummary       Unicode compliant Open source Ol Chiki font
%global fonts            *.ttf
%global fontconfs        66-0-%{fontpkgname}.conf
BuildRequires: fontforge 
%global fontdescription  %{expand:
 This is an Unicode compliant Ol Chiki or Ol Cemet font
 Ol Chiki is a modern alphabetic script used to write Santhali 
 language. 
}
%fontpkg 

%prep
%forgesetup
 chmod 755 generate.pe
./generate.pe *.sfd

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sat Feb 05 2022 14:10:14 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.0-2
- chaged to forgesetup from forgeurl 
- modified dtd line in fontconfig 

* Thu Feb 03 2022 20:56:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.0-1
- First relase 