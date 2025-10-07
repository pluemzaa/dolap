<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="testlab4_1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:36:17 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzowMzo0NCBQTTsyNTQz"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzozNjoxNyBQTTsxOzI2NTc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <declare name="Child, Adult" type="Integer" array="False" size=""/>
            <declare name="childPrice, adultPrice, total" type="Integer" array="False" size=""/>
            <assign variable="childPrice" expression="120"/>
            <assign variable="adultPrice" expression="189"/>
            <assign variable="total" expression="0"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="Child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="Adult"/>
            <output expression="&quot;You ordered&quot;&amp;Child&amp;&quot;children and&quot;&amp;Adult&amp;&quot;adults&quot;" newline="True"/>
            <assign variable="Child" expression="Child*120"/>
            <assign variable="Adult" expression="Adult*189"/>
            <assign variable="total" expression="Child+Adult"/>
            <output expression="&quot;Total price:&quot;&amp;total&amp;&quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>