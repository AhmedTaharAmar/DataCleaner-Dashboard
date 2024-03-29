from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import *

@api_view(["GET"])
def get_utilisateurs(request):
    utilisateurs = User.objects.all()
    serializer = UsersSerializer(utilisateurs, many=True)

    return Response(serializer.data)

@api_view(["POST"])
def add_utilisateur(request):
    # new_user = {
    #     "username": "admin2",
    #     "email": "admin2@example.com",
    #     "password": "azerty",
    #     "is_staff": true,
    #     "is_superuser": true
    # }
    # serializer = UsersSerializer(data=new_user)
    
    serializer = UsersSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(["GET"])
def get_sales_by_products(request):
    top = request.query_params.get("top", None)
    year = request.query_params.get("year", None)
    limite = "LIMIT {}".format(top) if top else ""
    where = "WHERE extract(year from invoice_date) = {}".format(year) if year else ""

    requeteSQL = """
        SELECT (1) AS id, stock_code, COUNT(*) AS nb_ventes
            FROM details_commande AS dc
                INNER JOIN produit AS pr
                    ON dc.stock_code_id = pr.stock_code
            {}
            GROUP BY (1), stock_code
            ORDER BY nb_ventes DESC
            {};
    """.format(where, limite)

    sales_by_products = Produit.objects.raw(requeteSQL)
    serializer = SalesByProductsSerializer(sales_by_products, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_sales_by_countries(request):
    top = request.query_params.get("top", None)
    year = request.query_params.get("year", None)
    limite = "LIMIT {}".format(top) if top else ""
    where = "WHERE extract(year from invoice_date) = {}".format(year) if year else ""

    requeteSQL = """
        SELECT (1) AS id, country, COUNT(*) AS nb_ventes
            FROM details_commande AS dc
                INNER JOIN commande AS co
                    ON dc.invoice_no_id = co.invoice_no
                INNER JOIN pays AS pa
                    ON co.country_id = pa.country
            {}
            GROUP BY (1), country
            ORDER BY nb_ventes DESC
            {};
    """.format(where, limite)

    sales_by_countries = User.objects.raw(requeteSQL)
    serializer = SalesByCountriesSerializer(sales_by_countries, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_sales_of(request):
    pays = request.query_params.get("pays", None)
    top = request.query_params.get("top", None)
    where = "WHERE country = '{}'".format(pays) if pays else ""
    print(where)
    limite = "LIMIT {}".format(top) if top else ""

    requeteSQL = """
        SELECT (1) AS id, country, stock_code, COUNT(*) AS nb_ventes
            FROM details_commande AS dc
                INNER JOIN produit AS pr
                    ON dc.stock_code_id = pr.stock_code
                INNER JOIN commande AS co
                    ON dc.invoice_no_id = co.invoice_no
                INNER JOIN pays AS pa
                    ON co.country_id = pa.country
            {}
            GROUP BY (1), country, stock_code
            ORDER BY nb_ventes DESC
            {};
    """.format(where, limite)

    sales_of = User.objects.raw(requeteSQL)
    serializer = SalesOfSerializer(sales_of, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_countries(request):
    requeteSQL = """
        SELECT (1) AS id, *
            FROM pays
            ORDER BY country ASC;
    """

    countries = Pays.objects.raw(requeteSQL)
    serializer = CountriesSerializer(countries, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_years(request):
    requeteSQL = """
        SELECT (1) AS id, EXTRACT(YEAR FROM invoice_date) AS year
            FROM details_commande
            GROUP BY year
            ORDER BY year DESC;
    """

    years = Details_commande.objects.raw(requeteSQL)
    serializer = YearsSerializer(years, many=True)

    return Response(serializer.data)
