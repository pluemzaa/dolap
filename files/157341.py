<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_403"/>
        <attribute name="authors" value="K"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 08:01:26 AM"/>
        <attribute name="created" value="SztERVNLVE9QLTY1TEZVTEo7MjU2OC0wNy0xODswNzo1NTozMyBBTTsyNDM1"/>
        <attribute name="edited" value="SztERVNLVE9QLTY1TEZVTEo7MjU2OC0wNy0xODswODowMToyNiBBTTsxOzI1Mzc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i &lt;=n">
                <output expression="&quot;&quot;&amp;i&amp;&quot;&quot;" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>