from settings.baseUrl import baseURL


def prepareUrl(title, objIds=None):
    url = baseURL

    if title == "remove cat par":
        cat_id = int(objIds[0])
        return url + "product/cat/par/{}/".format(cat_id)

    elif title == "add cat par":
        cat_id = int(objIds[0])
        par_id = int(objIds[1])
        return url + "product/cat/par/{}/{}/".format(cat_id, par_id)

    elif title == "cat par list":
        cat_id = int(objIds[0])
        return url + "product/cat/par/ls/{}/".format(cat_id)

    elif title == "get or delete or edit cat":
        cat_id = int(objIds[0])
        return url + "product/cat/crud/{}/".format(cat_id)

    elif title == "add cat":
        return url + "product/cat/crud/"

    elif title == "cat list":
        return url + "product/cat/all/"

    elif title == "add prod":
        cat_id = int(objIds[0])
        return url + "product/p/{}/".format(cat_id)

    elif title == "edit prod":
        cat_id = int(objIds[0])
        prod_id = int(objIds[1])
        return url + "product/p/{}/{}/".format(cat_id, prod_id)

    elif title == "get or delete prod":
        prod_id = int(objIds[0])
        return url + "product/g_d/{}/".format(prod_id)

    elif title == "prod list":
        cat_id = int(objIds[0])
        return url + "product/ls/{}/".format(cat_id)

    elif title == "add prod insta perm":
        prod_id = int(objIds[0])
        return url + "product/perm/{}/".format(prod_id)

    elif title == "get or delete or edit attr":
        attr_id = int(objIds[0])
        return url + "product/attr/cr/{}/".format(attr_id)

    elif title == "add attr":
        prod_id = int(objIds[0])
        return url + "product/attr/p/{}/".format(prod_id)

    elif title == "attr list":
        prod_id = int(objIds[0])
        return url + "product/attr/ls/{}/".format(prod_id)

    elif title == "add prod img":
        prod_id = int(objIds[0])
        return url + "product/img/p/{}/".format(prod_id)

    elif title == "prod img list":
        prod_id = int(objIds[0])
        return url + "product/img/ls/{}/".format(prod_id)

    elif title == "delete prod img":
        img_id = int(objIds[0])
        return url + "product/img/cr/{}/".format(img_id)

    elif title == "prod prop list":
        prod_id = int(objIds[0])
        return url + "product/prop/ls/{}/".format(prod_id)

    elif title == "get or delete or edit prod prop":
        prop_id = int(objIds[0])
        return url + "product/prop/cr/{}/".format(prop_id)

    elif title == "add prod prop":
        prod_id = int(objIds[0])
        return url + "product/prop/p/{}/".format(prod_id)
