#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sde
Version  : 2.0.15
Release  : 13
URL      : https://cran.r-project.org/src/contrib/sde_2.0.15.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sde_2.0.15.tar.gz
Summary  : Simulation and Inference for Stochastic Differential Equations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-sde-lib = %{version}-%{release}
BuildRequires : R-fda
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
Stochastic Differential Equations With R Examples, ISBN
        978-0-387-75838-1, Springer, NY.

%package lib
Summary: lib components for the R-sde package.
Group: Libraries

%description lib
lib components for the R-sde package.


%prep
%setup -q -c -n sde

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552945839

%install
export SOURCE_DATE_EPOCH=1552945839
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sde
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sde
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sde
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  sde || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sde/DESCRIPTION
/usr/lib64/R/library/sde/INDEX
/usr/lib64/R/library/sde/Meta/Rd.rds
/usr/lib64/R/library/sde/Meta/data.rds
/usr/lib64/R/library/sde/Meta/features.rds
/usr/lib64/R/library/sde/Meta/hsearch.rds
/usr/lib64/R/library/sde/Meta/links.rds
/usr/lib64/R/library/sde/Meta/nsInfo.rds
/usr/lib64/R/library/sde/Meta/package.rds
/usr/lib64/R/library/sde/Meta/vignette.rds
/usr/lib64/R/library/sde/NAMESPACE
/usr/lib64/R/library/sde/R/sde
/usr/lib64/R/library/sde/R/sde.rdb
/usr/lib64/R/library/sde/R/sde.rdx
/usr/lib64/R/library/sde/book/ch1.R
/usr/lib64/R/library/sde/book/ch2.R
/usr/lib64/R/library/sde/book/ch3.R
/usr/lib64/R/library/sde/book/ch4.R
/usr/lib64/R/library/sde/book/ex1.01.R
/usr/lib64/R/library/sde/book/ex1.02.R
/usr/lib64/R/library/sde/book/ex1.03.R
/usr/lib64/R/library/sde/book/ex1.04.R
/usr/lib64/R/library/sde/book/ex1.05.R
/usr/lib64/R/library/sde/book/ex1.06.R
/usr/lib64/R/library/sde/book/ex1.07.R
/usr/lib64/R/library/sde/book/ex1.08.R
/usr/lib64/R/library/sde/book/ex1.09.R
/usr/lib64/R/library/sde/book/ex1.10.R
/usr/lib64/R/library/sde/book/ex1.11.R
/usr/lib64/R/library/sde/book/ex1.12.R
/usr/lib64/R/library/sde/book/ex1.13.R
/usr/lib64/R/library/sde/book/ex1.14.R
/usr/lib64/R/library/sde/book/ex1.15.R
/usr/lib64/R/library/sde/book/ex2.01.R
/usr/lib64/R/library/sde/book/ex2.02.R
/usr/lib64/R/library/sde/book/ex2.03.R
/usr/lib64/R/library/sde/book/ex2.04.R
/usr/lib64/R/library/sde/book/ex2.05.R
/usr/lib64/R/library/sde/book/ex2.06.R
/usr/lib64/R/library/sde/book/ex2.07.R
/usr/lib64/R/library/sde/book/ex2.08.R
/usr/lib64/R/library/sde/book/ex2.09.R
/usr/lib64/R/library/sde/book/ex2.10.R
/usr/lib64/R/library/sde/book/ex2.11.R
/usr/lib64/R/library/sde/book/ex2.12.R
/usr/lib64/R/library/sde/book/ex2.13.R
/usr/lib64/R/library/sde/book/ex2.14.R
/usr/lib64/R/library/sde/book/ex2.15.R
/usr/lib64/R/library/sde/book/ex2.16.R
/usr/lib64/R/library/sde/book/ex2.17.R
/usr/lib64/R/library/sde/book/ex2.18.R
/usr/lib64/R/library/sde/book/ex3.01.R
/usr/lib64/R/library/sde/book/ex3.02.R
/usr/lib64/R/library/sde/book/ex3.03.R
/usr/lib64/R/library/sde/book/ex3.04.R
/usr/lib64/R/library/sde/book/ex3.05.R
/usr/lib64/R/library/sde/book/ex3.06.R
/usr/lib64/R/library/sde/book/ex3.07.R
/usr/lib64/R/library/sde/book/ex3.08.R
/usr/lib64/R/library/sde/book/ex3.09.R
/usr/lib64/R/library/sde/book/ex3.10.R
/usr/lib64/R/library/sde/book/ex3.11.R
/usr/lib64/R/library/sde/book/ex3.12.R
/usr/lib64/R/library/sde/book/ex3.13.R
/usr/lib64/R/library/sde/book/ex3.14.R
/usr/lib64/R/library/sde/book/ex3.15.R
/usr/lib64/R/library/sde/book/ex3.16.R
/usr/lib64/R/library/sde/book/ex4.01.R
/usr/lib64/R/library/sde/book/ex4.02.R
/usr/lib64/R/library/sde/book/ex4.03.R
/usr/lib64/R/library/sde/book/ex4.04.R
/usr/lib64/R/library/sde/book/ex4.05.R
/usr/lib64/R/library/sde/book/ex4.06.R
/usr/lib64/R/library/sde/book/ex4.07.R
/usr/lib64/R/library/sde/data/DWJ.rda
/usr/lib64/R/library/sde/data/quotes.rda
/usr/lib64/R/library/sde/doc/changes.txt
/usr/lib64/R/library/sde/doc/index.html
/usr/lib64/R/library/sde/doc/sde.errata.Rnw
/usr/lib64/R/library/sde/doc/sde.errata.pdf
/usr/lib64/R/library/sde/help/AnIndex
/usr/lib64/R/library/sde/help/aliases.rds
/usr/lib64/R/library/sde/help/paths.rds
/usr/lib64/R/library/sde/help/sde.rdb
/usr/lib64/R/library/sde/help/sde.rdx
/usr/lib64/R/library/sde/html/00Index.html
/usr/lib64/R/library/sde/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sde/libs/sde.so
/usr/lib64/R/library/sde/libs/sde.so.avx2
/usr/lib64/R/library/sde/libs/sde.so.avx512
