# SPDX-License-Identifqier: MIT

Version:   1.0.0

Release:   1

URL: https://github.com/mitradranirban/uniol-fonts

%global fontfamily    uniol        

%global fontlicense       OFL

%global fontlicenses      LICENCE.txt

%global fontdocs          *.txt

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
Source0:  https://raw.githubusercontent.com/mitradranirban/uniol-fonts/main/uniol-fonts-1.0.0.tar.gz

%fontpkg 

%prep

%setup -q -n %{fontfamily}-fonts-%{version} 
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

* Thu Feb 03 2022 20:56:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.0-1
-
