<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="12345"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:24:42 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzoxNzozNyBQTTsyNTUw"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzoyNDo0MiBQTTsxOzI2NTI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="childPrice, adultPrice, numch, numad, total" type="Integer" array="False" size=""/>
            <assign variable="childPrice" expression="120"/>
            <assign variable="adultPrice" expression="189"/>
            <assign variable="total" expression="0"/>
            <output expression="&quot;Price List: &quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person &quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="numch"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="numad"/>
            <assign variable="total" expression="(numch * 120) + (numad * 189)"/>
            <output expression="&quot;You ordered &quot; &amp; numch &amp;&quot; children and &quot;&amp; numad &amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>