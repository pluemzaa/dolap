<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test3_lab4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 03:39:28 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MzE6MTggUE07MjU3Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6Mzk6MjggUE07MTsyNjk0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Enter n:&quot;" newline="True"/>
            <input variable="n"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; n">
                <output expression="&quot;Round&quot; &amp; (i+1)" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>