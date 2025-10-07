<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3618;&#3634;&#3585;"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 05:04:35 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MzY6MzAgUE07MjU3Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NDc6NTIgUE07Mztjb21wdXRlcjtDUC1DT007MjAyNS0wNy0xNjswMzo0MTo1MiBQTTtNb25leS5mcHJnOzYzODQ="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MDQ6MzUgUE07MTsyNjg2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, vat, total, sum" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="vat"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <assign variable="money" expression="money * (1+(vat/100))"/>
                <assign variable="i" expression="i + 1"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;:&quot; &amp; money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>