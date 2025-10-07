<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:41:46 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDE6MDE6MTcgUE07MjU3MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDE6NDYgUE07OTsyNjk0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="total, child, adult" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="child"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="adult"/>
            <assign variable="total" expression="(child*120) + (adult*189)"/>
            <output expression="&quot;You ordered &quot; &amp; child &amp; &quot; children&quot; &amp; &quot; and &quot; &amp; adult &amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>