class TOKENISED:
    def __init__(self,keyword: str):
        match keyword:
            case "wait":
                self.type = "WAIT_STATEMENT"
            case "awoo":
                self.type = "AWOOO_END"
            case "like":
                self.type = "VAR_DECL_START"
            case "fr":
                self.type = "VAR_DECL_END"
            case "rizz":
                self.type = "PRIORITY_STATEMENT"
            case "baddies":
                self.type = "VAR_REF_START"
            case "using":
                self.type = "VAR_REF_END"
            case "self":
                self.type = "SELF_REF"
        # end because i haven't decided on more yet