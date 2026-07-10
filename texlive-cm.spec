%global tl_name cm
%global tl_revision 57963

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Computer Modern fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cm
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Knuth's final iteration of his re-interpretation of a c.19 Modern-style
font from Monotype. The family is comprehensive, offering both sans and
roman styles, and a monospaced font, together with mathematics fonts
closely integrated with the mathematical facilities of TeX itself. The
base fonts are distributed as Metafont source, but autotraced PostScript
Type 1 versions are available (one version in the AMS fonts
distribution, and also the BaKoMa distribution). The Computer Modern
fonts have inspired many later families, notably the European Computer
Modern and the Latin Modern families.

