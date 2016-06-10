# Documentation: https://github.com/Homebrew/brew/blob/master/share/doc/homebrew/Formula-Cookbook.md
#                http://www.rubydoc.info/github/Homebrew/brew/master/Formula
# PLEASE REMOVE ALL GENERATED COMMENTS BEFORE SUBMITTING YOUR PULL REQUEST!

class HomebrewCmd < Formula
  desc ""
  homepage ""
  url "https://github.com/cundohubs/homebrew-cmd/archive/0.0.3.tar.gz"
  version "0.0.3"
  sha256 "e86d36147282c74ca812632d421ec8cf9844a74549c8aaf7facd3703acb0af71"


  def install
    # ENV.deparallelize  # if your formula fails when building in parallel
    bin.install "curalate"
  end

end
