# ========================================================
# Using **kwargs for Arbitrary Keyword Arguments
# ========================================================
def userprofile(**kwargs):
    print("User Profile:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
userprofile(name="deepak" , age=22 , area="velacherri")