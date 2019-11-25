# Title: Most frequently used words in a text
# Source: codewars.com
# Site: https://www.codewars.com/kata/51e056fe544cf36c410000fb
# Code by: Vikash Singh
#
# Description:
# Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of
# the top-3 most occurring words, in descending order of the number of occurrences.
#
# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to
# handle fancy punctuation.)
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an
# empty array if a text contains no words.
# Examples:
# top_3_words("In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.")
# # => ["a", "of", "on"]
#
# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# # => ["e", "ddd", "aa"]
#
# top_3_words("  //wont won't won't")
# # => ["won't", "wont"]


from collections import Counter


def replace_special_character(text):
    special_character = ".\\-/,:_;~!@#$%^&*()_+={}|<>?"
    new_string = ""
    for x in special_character:
        text = text.replace(x, " ")

    for x in range(len(text)-1):
        if not (text[x] == "'" and not text[x+1] in "abcderfghijklmnopqrstuvwxyz"):
            new_string += text[x]
        elif text[x] == "'" and x > 0:
            if text[x-1] in "abcderfghijklmnopqrstuvwxyz":
                new_string += text[x]
    return new_string + text[len(text)-1] if len(text) > 0 else new_string


def top_3_words(texts):
    # print(texts)
    texts = replace_special_character(texts.lower()).lower().split(" ")
    words = [x for x in texts if len(x) > 0]
    dict_words = Counter(words)
    return [x[0] for x in dict_words.most_common(3)]


# Sample Examples
# sentence = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."
# sentence = "  , e   .. "
# sentence = "a a a  b  c c  d d d d  e e e e e"
# sentence = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
# sentence = "//wont Won't won't user's'''"
# sentence = "  , e   .. "
# sentence = "  ...  "
# sentence = "  '  "
# sentence = "  '''  "
# sentence = "a a a  b  c c X"

# sentence = "VtByfmCl/,BVHkGSKq,,_hSfWrrs:_/_;XnoMEec?_-:/UmdnXJwhVy:;!webheIEM .,-_hSfWrrs -__;BVHkGSKq- :-XnoMEec-_Mhvdeev_;!_webheIEM-!BVHkGSKq,?.:VtByfmCl!:CUMjPWxa/;/ wGySvq_!-,CUMjPWxa/:.XnoMEec,.?/!BVHkGSKq.?,?_UmdnXJwhVy?!?.UmdnXJwhVy -. -Mhvdeev;XnoMEec,_;BVHkGSKq-_!,?BVHkGSKq/,XnoMEec:_?-,VtByfmCl-:-:hSfWrrs?:!??BVHkGSKq_!;;BVHkGSKq.;XnoMEec-UmdnXJwhVy,VtByfmCl?.?-:wGySvq?BVHkGSKq/;.Mhvdeev!/-Mhvdeev?VtByfmCl ./__XnoMEec.vjhgl:_!:XnoMEec. .-VtByfmCl-,,webheIEM:wGySvq?BVHkGSKq_:.?!CUMjPWxa!BVHkGSKq:..,XnoMEec,!.Mhvdeev:XnoMEec ;/?BVHkGSKq!vjhgl__/UmdnXJwhVy!, ?:hSfWrrs;_;XnoMEec-?.XnoMEec:/ XnoMEec,.UmdnXJwhVy/ XnoMEec?:Mhvdeev/BVHkGSKq: -:_hSfWrrs-  ?-UmdnXJwhVy,;/wGySvq;.;.Mhvdeev.:/hSfWrrs :Mhvdeev_?.XnoMEec/CUMjPWxa?-_UmdnXJwhVy Mhvdeev.!_,!CUMjPWxa /Mhvdeev:! /Mhvdeev .CUMjPWxa:.;:,XnoMEec.BVHkGSKq//UmdnXJwhVy;,!CUMjPWxa_.:-/VtByfmCl.Mhvdeev_;,.Mhvdeev; CUMjPWxa?:XnoMEec/!:,CUMjPWxa::-- CUMjPWxa:?- UmdnXJwhVy;_ BVHkGSKq? ?_!hSfWrrs;;.Mhvdeev?/:UmdnXJwhVy,.;/BVHkGSKq,?Mhvdeev;.! BVHkGSKq XnoMEec_,BVHkGSKq._-_UmdnXJwhVy :!;;UmdnXJwhVy!:!-!vjhgl;-_;:BVHkGSKq-?:!hSfWrrs_Mhvdeev.._;Mhvdeev :-XnoMEec-XnoMEec.!_XnoMEec/ :VtByfmCl!?,Mhvdeev;-BVHkGSKq__!CUMjPWxa!/BVHkGSKq:/!-!CUMjPWxa:vjhgl,,;!BVHkGSKq.Mhvdeev-:!/?wGySvq-,-BVHkGSKq:.?/?wGySvq/:.! vjhgl_-,,vjhgl XnoMEec-BVHkGSKq;-/VtByfmCl-_/;XnoMEec? CUMjPWxa;-/Mhvdeev.:BVHkGSKq ?._,hSfWrrs?_;BVHkGSKq-!BVHkGSKq ??hSfWrrs_ ?.:"
sentence = "sxLgWwYCQ-YOHeZga:-sxLgWwYCQ-._ ?YOHeZga,;?-.jJIn/ZkBEuqKay/jJIn!YOHeZga./: :jJIn;uq'_/;uq',,;!/CBZ--:YOHeZga:TcQCd?_/uq'-..jJIn,--/YOHeZga !sxLgWwYCQ?_sxLgWwYCQ;,,!;uSVxB,.uq'-?;jJIn!?YOHeZga!/ !.ubBsADf/__ZkBEuqKay,YOHeZga-,/CBZ-YOHeZga,bjBDBOjX :?: ZkBEuqKay;!?_bjBDBOjX;-CBZ :/uq';./uq'._/-TcQCd?_--,sxLgWwYCQ! sxLgWwYCQ:?!:?CBZ-?ZkBEuqKay.,sxLgWwYCQ?ZkBEuqKay?/:sxLgWwYCQ-.,YOHeZga/;_/ TcQCd;_./uq':ZkBEuqKay ,ubBsADf?_  -sxLgWwYCQ?!;?.uq'?-,epWG?sxLgWwYCQ:TcQCd._jJIn,CBZ__ ;,sxLgWwYCQ: TcQCd:  zUi-/,zUi?_!/bjBDBOjX. ,;ubBsADf:;:/,CBZ_ jJIn _?;:sxLgWwYCQ.YOHeZga.ubBsADf??.-.uq': :._zUi:YOHeZga,?! ?TcQCd/!/ZkBEuqKay!YOHeZga?:!uq'?!;;uq'!:_, zUi/-CBZ_/, :CBZ;/!!YOHeZga,.;?uq'!,;;ZkBEuqKay?epWG!;-ZkBEuqKay?/,:;uSVxB;ZkBEuqKay_,YOHeZga_//uq'/;,,zUi_,. uSVxB-?:;sxLgWwYCQ?sxLgWwYCQ;sxLgWwYCQ?CBZ_ ?:sxLgWwYCQ! ;:ZkBEuqKay_TcQCd  ubBsADf -. ?CBZ;?!.sxLgWwYCQ!_/_:CBZ?-uq';zUi??-sxLgWwYCQ-sxLgWwYCQ!,!;,jJIn ZkBEuqKay:.,uq' ?-/ZkBEuqKay/YOHeZga,CBZ-:; CBZ/ :- TcQCd/.zUi,/.!uq'_?YOHeZga,/;sxLgWwYCQ?_! _zUi/uq';?-_YOHeZga!/??:jJIn/;?-YOHeZga:;bjBDBOjX/zUi;!-; CBZ/,.ZkBEuqKay ; TcQCd --ZkBEuqKay!,;_!YOHeZga?jJIn!!CBZ?sxLgWwYCQ/ZkBEuqKay;?  ,zUi,-!YOHeZga,!zUi//bjBDBOjX_uq'/ uq'!!-:jJIn/:_uq'__!.zUi;!-.,jJIn?uSVxB/:/_-zUi.-,sxLgWwYCQ/zUi/-/!zUi/:?CBZ:?ubBsADf?-ubBsADf?._.TcQCd?::TcQCd_?:_ZkBEuqKay-:!;jJIn-,zUi!jJIn ,-sxLgWwYCQ-//!/zUi-?/TcQCd.uq'.:-uq'-!;:epWG/?YOHeZga.-uSVxB_uq'_,!CBZ/?- CBZ/,:YOHeZga-CBZ/;./,ZkBEuqKay!!:CBZ;._YOHeZga!,_-uSVxB:_ "

print(top_3_words(sentence))

