'''
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?

'''
def oops_index_error():
    raise IndexError

def oops_key_error():
    raise KeyError


def catch_error():
    try:
        oops_key_error()
    except IndexError:
        print("index error catched")
    except KeyError:
        print("key error catched")
    except:
        print("unknown error catched")

if __name__ == "__main__":
    catch_error()