# CYS - 49 53 20 54 48 49 53 20 48 45 58 3f
CYS

## Challenge 

DESCRIPTION
Cyber Youth Singapore Sponsor Challenge

I find hex very cool :D


ATTACHED FILES
flag.docx

## Solution

### second part

use strings

	 $ strings flag.docx | tail
	....omg wow 2/3:...._1s_c0


### third part

Copy all text in the docx

	wow u found me :o 3/3 :
	30 6c 5f 3c 33 7d

### first part
	
inside comments

	$ grep -rnw './' -e '1/3'
	<w:t>woo u found the first part</w:t></w:r><w:r w:rsidR="000A66FF"><w:t xml:space="preserve"> 1/3</w:t></w:r><w:r><w:t>: WH2020{H3x</w:t></w:r><w:bookmarkStart w:id="2" w:name="_GoBack"/><w:bookmarkEnd w:id="2"/><w:r><w:t xml:space="preserve">                                                                                                                      </w:t></w:r></w:p></w:comment></w:comments>


## Flag

	WH2020{H3x_1s_c00l_<3}