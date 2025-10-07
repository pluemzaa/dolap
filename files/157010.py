<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowLab1"/>
        <attribute name="authors" value="Ninen"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:09:38 PM"/>
        <attribute name="created" value="TmluZW47U0FCVFVERTsyMDI1LTA3LTE2OzAzOjU3OjQ2IFBNOzIzMTY="/>
        <attribute name="edited" value="TmluZW47U0FCVFVERTsyMDI1LTA3LTE2OzA0OjA5OjM4IFBNOzE7MjQyMw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="children, adult, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adult"/>
            <assign variable="total" expression="(children*120)+(adult*189)"/>
            <output expression="&quot;You ordered &quot; &amp;children&amp; &quot; children and &quot; &amp;adult&amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>