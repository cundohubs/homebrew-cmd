# Documentation: https://github.com/Homebrew/brew/blob/master/share/doc/homebrew/Formula-Cookbook.md
#                http://www.rubydoc.info/github/Homebrew/brew/master/Formula

class Homebrewcmd < Formula
  desc ""
  homepage ""
  url "https://github.com/cundohubs/homebrew-cmd/archive/0.0.4.tar.gz"
  version "0.0.3"
  sha256 "6d969d7340090e228573b7a4800712835ba9411d6f0cf7fce813f714d8164088"


  def install
    # ENV.deparallelize  # if your formula fails when building in parallel
    bin.install "curalate"
  end

end
