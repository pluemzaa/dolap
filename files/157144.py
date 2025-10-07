<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="mu kata_lab4"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:10:30 PM"/>
        <attribute name="created" value="QWRtaW47TEFQVE9QLUJLNFRIREpIOzI1NjgtMDctMTY7MDU6NDk6NDIgUE07Mjg2NA=="/>
        <attribute name="edited" value="QWRtaW47TEFQVE9QLUJLNFRIREpIOzI1NjgtMDctMTY7MDY6MTA6MzAgUE07MTsyOTU4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <declare name="children" type="Integer" array="False" size=""/>
            <declare name="adults" type="Integer" array="False" size=""/>
            <declare name="total" type="Integer" array="False" size=""/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(children * 120) + (adults * 189)"/>
            <output expression="&quot;You ordered &quot; &amp; children &amp; &quot; children and &quot;  &amp; adults &amp;&quot; adults &quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht &quot;" newline="True"/>
            <output expression="&quot; Enjoy your meal! &quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>