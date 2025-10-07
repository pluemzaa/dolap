<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab 3"/>
        <attribute name="authors" value="poori"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-23 08:43:33 PM"/>
        <attribute name="created" value="cG9vcmk7UE9PUklQQVQ7MjAyNS0wNy0yMzswODo0MTozNCBQTTsyNDYw"/>
        <attribute name="edited" value="cG9vcmk7UE9PUklQQVQ7MjAyNS0wNy0yMzswODo0MzozMyBQTTsxOzI1Njk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i &lt;= n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>