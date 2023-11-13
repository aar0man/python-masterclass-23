from collections import deque
from utils import timeit

original_string = "masterclass"
original_string = """
    Join us for an exciting Python masterclass and unlock the power of Python programming! 
    Dive into the world of Python, where you'll learn the fundamentals, advanced techniques, and best practices. 
    Our expert instructors will guide you through hands-on projects and real-world applications,
    making this masterclass a must-attend for both beginners and experienced developers. 
    Don't miss this opportunity to elevate your Python skills to the next level!
"""
original_string = """
    Welcome to the ultimate Python Masterclass, an immersive journey into the heart of Python programming. 
    Our masterclass is designed to cater to all levels of expertise, whether you're a complete beginner or a seasoned developer 
    looking to enhance your Python skills.
    In this comprehensive program, you will explore the Python language from its basic syntax to advanced topics 
    like data science, web development, and machine learning. Our expert instructors will provide you with hands-on 
    experience, guiding you through projects that mirror real-world applications, giving you the practical skills you need to succeed.
    But it's not just about code; we'll delve into the best practices, design patterns, and tips and tricks that only 
    seasoned Python developers know. By the end of this masterclass, you'll have a strong foundation in Python and 
    the ability to tackle complex coding challenges with confidence.
    Come join us for this Python Masterclass, and get ready to unleash your coding potential, make your mark in the 
    Python community, and advance your career in one of the most versatile and in-demand programming languages around.
"""
original_string = """
    W££lcom€ to th€ µlt!mát€ P¥thon Màster©lass, àη ιmm€rs!v€ jöµrn€¥ !nto th€ h€art öf Pythön prôgramm!ng. Öur mà$t€r©lass !s d€s!gn€d to càt€r to all 
    lev€ls öf €xþ€rt!s€, wh€th€r ¥oµ'r€ à çömp!€t€ b€g!nn€r ör à s€àsön€d d€v€löp€r løök!ng to ënhàn©€ ¥oµr P¥thön $k!ll$.
    !n th!$ ©ömp®€h€n$!v€ próg®àm, yoµ w!ll €xp!or€ th€ P¥thön làngµàg€ fröm !t$ bà$!ç $¥ntàx to àdvàn©€d tòp!©$ l!k€ dàtà 
    $©!€n©€, w€b d€v€löpm€nt, ànd mà©h!n€ lààrn!ng. Öµ® €xp€®t !n$trµ©t®®$ w!ll þ®ov!d€ ¥oµ w!th hånds-ön €xp€®!€nc€, 
    gµ!d!ng ¥oµ th®oµgh þ®oje©t$ thàt m!®®o® ®€àl-wö®ld àþþl!©àt!öns, g!v!ng ¥oµ th€ þ®à©t!©àl $k!ll$ yoµ né€d to $µ©©€€d.
    ßµt !t'$ not jµ$! aboµt ©od€; w€'ll Ð€lv€ !nto th€ b€$t þ®à©t!©€$ , d€$!gn þàtt€®n$, ànd t!þ$ ànd t®!©k$ thàt 
    önl¥ $€à$on€d P¥thön d€v€löp€®$ knöw. ß¥ th€ €nd öf th!$ mà$t€®©lass, yoµ'll håv€ à $t®ong föµndàt!on !n P¥thön 
    ànd th€ àb!l!t¥ to tà©kl€ ©ompl€x ©od!ng ©hàll€ng€$ w!th ©onf!d€n©€.
    ©om€ jo!n µ$ fö® th!$ P¥thön Màst€®©lass, ànd g€t ®€àd¥ to µnl€à$h€ ¥oµ® ©od!ng þot€nt!àl, måk€ ¥oµ® mà®k !n th€ 
    P¥thön ©ommµn!t¥, ànd àdvàn©€ ¥oµ® ©à®€€® !n on€ öf th€ mø$t v€®$àt!l€ ànd !n-©€màn© þ®og®àmm!ng làngµàg€$ à®oµnd."
"""


@timeit
def without_map():
    _our_list = []     
    for i in original_string: 
        _our_list.append(i.upper())
    return _our_list


@timeit
def without_map_and_yield():
    for i in original_string: 
        yield i.upper()


@timeit
def with_map():
    return map(str.upper, original_string)  


@timeit
def process_data(_data_without_map):
    for i in _data_without_map:
        pass


@timeit
def process_data_deque(_data_without_map):
    for i in deque(_data_without_map):
        pass


masterclass_word = 'masterclass'
# masterclass_word = 'jdifhasuiodfh8asdghfasyuadsjkhfoauisdfoaisjcdapidhvouiwahjcoiaHJFVUIASDCO;JCSdvhasidufhaSIFHasuiodvhasudiohgfaipsjdfpSEDHGFVUOHVRD9CPJASopicfhjwefvh'


@timeit
def check_key_in_dict(_alphabet_dict):
    for w in masterclass_word: 
        if w not in _alphabet_dict: 
            _alphabet_dict[w] = 0
        _alphabet_dict[w] += 1
    return _alphabet_dict  



@timeit
def check_key_in_dict_with_try(_alphabet_dict):
    for w in _alphabet_dict: 
        try: 
            _alphabet_dict[w] += 1
        except KeyError: 
            _alphabet_dict[w] = 1
    return _alphabet_dict


class Masterclass: 
    def optimization(self, x):
        # print(x*x) 
        pass


@timeit
def call_class_method():
    for i in range(100):
        Masterclass().optimization(2)


@timeit
def call_class_method_with_variable():
    MasterclassObj = Masterclass()
    optimization = MasterclassObj.optimization
    for i in range(100):
        optimization(2)


if __name__ == '__main__':
    # part 1 ===================================================

    # data_without_map = without_map()
    # data_without_map_and_yield = without_map_and_yield()
    # data_with_map = with_map()
    #
    # print()
    #
    # process_data(data_without_map)
    # process_data(data_without_map_and_yield)
    # process_data(data_with_map)
    #
    # print()
    #
    # process_data_deque(data_without_map)
    # process_data_deque(data_without_map_and_yield)
    # process_data_deque(data_with_map)

    # part 2 ===================================================

    alphabet_dict = {letter: 1 for letter in masterclass_word}
    check_key_in_dict(alphabet_dict.copy())
    check_key_in_dict_with_try(alphabet_dict.copy())

    # part 3 ===================================================

    call_class_method()
    call_class_method_with_variable()


def get_random_string():  # example for lazy imports
    from utils import random_string
    return random_string()
