Name:		texlive-cm
Version:	20180303
Release:	2
Summary:	Computer Modern fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cm
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Knuth's final iteration of his re-interpretation of a c.19
Modern-style font from Monotype. The family is comprehensive,
offering both sans and roman styles, and a monospaced font,
together with mathematics fonts closely integrated with the
mathematical facilities of TeX itself. The base fonts are
distributed as Metafont source, but autotraced PostScript Type
1 versions are available (one version in the AMS fonts
distribution, and also the BaKoMa distribution). The Computer
Modern fonts have inspired many later families, notably the
European Computer Modern and the Latin Modern families.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/cm
%{_texmfdistdir}/fonts/pk/ljfour/public/cm
%{_texmfdistdir}/fonts/source/public/cm
%{_texmfdistdir}/fonts/tfm/public/cm
%doc %{_texmfdistdir}/doc/fonts/cm

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
